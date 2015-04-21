from datetime import datetime

def dated_default(obj):
  if isinstance(obj, datetime):
    return obj.isoformat()
