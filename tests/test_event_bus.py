from core.event_bus import EventBus


def test_event_bus():
    bus = EventBus()

    received = []

    def listener(event):
        received.append(event)

    bus.subscribe("test", listener)
    bus.emit("test", {"message": "Hello"})

    assert len(received) == 1
    assert received[0]["data"]["message"] == "Hello"

    print("✓ EventBus test passed")


if __name__ == "__main__":
    test_event_bus()