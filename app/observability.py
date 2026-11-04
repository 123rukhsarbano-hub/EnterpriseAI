"""Privacy-first Rius tracing. No telemetry is sent without RIUS_API_KEY."""
import os
import logging
from functools import wraps

log = logging.getLogger(__name__)

def initialize():
    """Call once, before instrumented app modules are loaded."""
    from dotenv import load_dotenv
    load_dotenv()
    if not os.getenv("RIUS_API_KEY") or os.getenv("RIUS_DISABLED", "false").lower() in ("1", "true", "yes"):
        log.info("RIUS tracing disabled (RIUS_API_KEY not set or RIUS_DISABLED=true)")
        return
    
    try:
        import rius
        rius.init(service_name=os.getenv("RIUS_SERVICE_NAME", "enterprise-ai-assistant"), capture_content=False)
        log.info("RIUS tracing enabled (RIUS_API_KEY set)")
    except Exception as e:
        log.warning(f"Failed to initialize RIUS tracing: {e}, application will continue without telemetry")
        
def trace(name):
    """Decorate sync/async functions; never export arguments or return values."""
    def decorate(fn):
        try:
            import rius
            return rius.observe(name=name, capture_input=False, capture_output=False)(fn)
        except ImportError:
            return fn
    return decorate