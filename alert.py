def check_alert(objects):
    suspicious_emotions = ["Angry", "Fear"]

    for obj_id, data in objects.items():
        (_, _, _, _, emotion) = data

        if emotion in suspicious_emotions:
            return True

    return False
