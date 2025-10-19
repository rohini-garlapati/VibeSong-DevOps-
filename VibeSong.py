from flask import Flask, render_template, request

app = Flask(__name__)

mood_songs = {
    "happy": [
        {"title": "Happy Vibes", "url": "https://www.youtube.com/embed/ZbZSe6N_BXs", "thumb": "https://i.ytimg.com/vi/ZbZSe6N_BXs/hqdefault.jpg"},
        {"title": "Dance All Day", "url": "https://www.youtube.com/embed/ru0K8uYEZWw", "thumb": "https://i.ytimg.com/vi/ru0K8uYEZWw/hqdefault.jpg"},
    ],
    "sad": [
        {"title": "Let It Go", "url": "https://www.youtube.com/embed/y6120QOlsfU", "thumb": "https://i.ytimg.com/vi/y6120QOlsfU/hqdefault.jpg"},
        {"title": "Someone Like You", "url": "https://www.youtube.com/embed/hLQl3WQQoQ0", "thumb": "https://i.ytimg.com/vi/hLQl3WQQoQ0/hqdefault.jpg"},
    ],
    "chill": [
        {"title": "Lofi Beats", "url": "https://www.youtube.com/embed/jfKfPfyJRdk", "thumb": "https://i.ytimg.com/vi/jfKfPfyJRdk/hqdefault.jpg"},
        {"title": "Rainy Mood", "url": "https://www.youtube.com/embed/1AhOK4UwAMs", "thumb": "https://i.ytimg.com/vi/1AhOK4UwAMs/hqdefault.jpg"},
    ],
    "energetic": [
        {"title": "Believer", "url": "https://www.youtube.com/embed/7wtfhZwyrcc", "thumb": "https://i.ytimg.com/vi/7wtfhZwyrcc/hqdefault.jpg"},
        {"title": "Thunder", "url": "https://www.youtube.com/embed/fKopy74weus", "thumb": "https://i.ytimg.com/vi/fKopy74weus/hqdefault.jpg"},
    ],
    "focus": [
        {"title": "Deep Focus Music", "url": "https://www.youtube.com/embed/2OEL4P1Rz04", "thumb": "https://i.ytimg.com/vi/2OEL4P1Rz04/hqdefault.jpg"},
        {"title": "Coding Music", "url": "https://www.youtube.com/embed/5qap5aO4i9A", "thumb": "https://i.ytimg.com/vi/5qap5aO4i9A/hqdefault.jpg"},
    ],
    "workout": [
        {"title": "Eye of the Tiger", "url": "https://www.youtube.com/embed/btPJPFnesV4", "thumb": "https://i.ytimg.com/vi/btPJPFnesV4/hqdefault.jpg"},
        {"title": "Stronger", "url": "https://www.youtube.com/embed/3M_5oYU-IsU", "thumb": "https://i.ytimg.com/vi/3M_5oYU-IsU/hqdefault.jpg"},
    ],
    "party": [
        {"title": "Uptown Funk", "url": "https://www.youtube.com/embed/OPf0YbXqDm0", "thumb": "https://i.ytimg.com/vi/OPf0YbXqDm0/hqdefault.jpg"},
        {"title": "Can't Stop the Feeling", "url": "https://www.youtube.com/embed/ru0K8uYEZWw", "thumb": "https://i.ytimg.com/vi/ru0K8uYEZWw/hqdefault.jpg"},
    ],
    "nostalgic": [
        {"title": "Let Her Go", "url": "https://www.youtube.com/embed/RBumgq5yVrA", "thumb": "https://i.ytimg.com/vi/RBumgq5yVrA/hqdefault.jpg"},
        {"title": "Fix You", "url": "https://www.youtube.com/embed/k4V3Mo61fJM", "thumb": "https://i.ytimg.com/vi/k4V3Mo61fJM/hqdefault.jpg"},
    ],
    "calm": [
    {"title": "Peaceful Piano", "url": "https://www.youtube.com/embed/1ZYbU82GVz4", "thumb": "https://i.ytimg.com/vi/1ZYbU82GVz4/hqdefault.jpg"},
    {"title": "Ocean Eyes", "url": "https://www.youtube.com/embed/riUBONxLABg", "thumb": "https://i.ytimg.com/vi/riUBONxLABg/hqdefault.jpg"},
]
}

@app.route("/", methods=["GET", "POST"])
def index():
    mood = None
    songs = []
    if request.method == "POST":
        mood = request.form["mood"]
        songs = mood_songs.get(mood, [])
        return render_template("music.html", mood=mood, songs=songs)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug =True)

