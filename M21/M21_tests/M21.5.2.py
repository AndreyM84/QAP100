class Event:
    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")
events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]
for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

# ответ
# 1554583508000
# 1555296337000
# 1549461608000
