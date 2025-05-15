class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"


class AudioMixin:
    def __init__(self, narrator, duration):
        self.narrator = narrator
        self.duration = duration  # e.g., in hours

    def play_audio(self):
        print(f"Playing audio narrated by {self.narrator} for {self.duration} hours.")

    def __str__(self):
        return f"Narrated by {self.narrator}, Duration: {self.duration} hrs"


class AudioBook(Book, AudioMixin):
    def __init__(self, title, author, narrator, duration):
        Book.__init__(self, title, author)
        AudioMixin.__init__(self, narrator, duration)

    def __str__(self):
        return f"AudioBook: '{self.title}' by {self.author} (Narrated by {self.narrator}, {self.duration} hrs)"


# Test it
audiobook = AudioBook("The Hobbit", "J.R.R. Tolkien", "Andy Serkis", 11)
print(audiobook)
audiobook.play_audio()
