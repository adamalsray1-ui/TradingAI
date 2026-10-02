import cv2, os, sys

VIDEO_DIR = "input_videos"
OUT_DIR = "frames"
EVERY_SECONDS = 2

def extract(video_path):
    os.makedirs(OUT_DIR, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total / fps if fps else 0

    name = os.path.splitext(os.path.basename(video_path))[0]
    folder = os.path.join(OUT_DIR, name)
    os.makedirs(folder, exist_ok=True)

    frame_no = 0
    saved = 0
    step = max(1, int(fps * EVERY_SECONDS))

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if frame_no % step == 0:
            path = os.path.join(folder, f"frame_{saved:06d}.jpg")
            cv2.imwrite(path, frame)
            saved += 1
        frame_no += 1

    cap.release()
    print(f"Video: {video_path}")
    print(f"Duration: {duration:.1f}s")
    print(f"Saved frames: {saved}")
    print(f"Output: {folder}")

if __name__ == "__main__":
    videos = [os.path.join(VIDEO_DIR, x) for x in os.listdir(VIDEO_DIR)
              if x.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))]
    if not videos:
        print("Put a trading video inside input_videos/")
    for v in videos:
        extract(v)
