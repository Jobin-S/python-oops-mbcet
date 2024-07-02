# Base Class
class Media:
    def __init__(self, title, creator, publish_year, genre):
        self.title = title
        self.creator = creator
        self.publish_year = publish_year
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Creator: {self.creator}")
        print(f"Publish Year: {self.publish_year}")
        print(f"Genre: {self.genre}")

    @staticmethod
    def search(media_list, **filters):
        results = []
        for media in media_list:
            match = True
            for key, value in filters.items():
                if hasattr(media, key) and getattr(media, key) != value:
                    match = False
                    break
            if match:
                results.append(media)
        return results

# Derived Class - Book
class Book(Media):
    def __init__(self, title, author, publish_year, genre, page_count):
        super().__init__(title, author, publish_year, genre)
        self.page_count = page_count

    def display_info(self):
        super().display_info()
        print(f"Author: {self.creator}")  # Creator is overridden by author
        print(f"Page Count: {self.page_count}")

# Derived Class - Magazine
class Magazine(Media):
    def __init__(self, title, creator, publish_year, genre, issue_number):
        super().__init__(title, creator, publish_year, genre)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

# Derived Class - Audiobook
class Audiobook(Book):
    def __init__(self, title, author, publish_year, genre, page_count, audio_length):
        super().__init__(title, author, publish_year, genre, page_count)
        self.audio_length = audio_length

    def display_info(self):
        super().display_info()
        print(f"Audio Length: {self.audio_length} hours")

# Example usage
book = Book("1984", "George Orwell", 1949, "Dystopian", 328)
magazine = Magazine("National Geographic", "Various", 2020, "Science", 202001)
audiobook = Audiobook("Becoming", "Michelle Obama", 2018, "Memoir", 464, 19.5)

media_list = [book, magazine, audiobook]

# Search and display filtered results
search_results = Media.search(media_list, genre="Dystopian")
for media in search_results:
    print("\nFiltered Search Result:")
    media.display_info()