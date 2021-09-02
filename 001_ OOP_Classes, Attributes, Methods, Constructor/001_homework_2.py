class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'This book "{self.title}" of the {self.genre} genre were written by {self.author} in {self.year}.'


class Resume:

    def __init__(self, resume):
        self.resume = resume

    def __str__(self):
        return self.resume


resume_cd = '''          “The Memoirs of Sherlock Holmes” was initially published in 1894 after each of 
    the individual stories contained within had appeared separately in The Strand magazine. This collection
    was the follow-up to “The Adventures of Sherlock Holmes” which introduced the detective
    and his loyal companion Dr. John Watson. The Memoirs are generally considered the superior
    to the collection which introduced the detective, but not as strong as the stories he solved
    in the next collection following his resurrection. The Memoirs of Sherlock Holmes
    draws to a close with Dr. John Watson disconsolate in his conviction that Holmes and
    his nemesis Prof. Moriarty fell to their deaths after a struggle atop Reichenbach Falls."'''

resume_sk = '''          “Bag of Bones” is a 1998 fantasy novel by American author Stephen King.
    Set in the fictional unincorporated town of TR-90, Maine, it follows an author,
    Mike Noonan, who suffers from writer’s block. Having isolated himself at his lake house to write,
    Noonan begins to experience delusions linked to the untimely death of his wife four years earlier.
    The plot borrows some of its tensions, events, and characterizations from Rebecca,
    a Gothic novel by English author Daphne du Maurier. Though not his most famous work,
    Bag of Bones is considered one of King’s best written and has been the recipient of many awards,
    including the British Fantasy Award for Best Novel and the Bram Stoker Award."'''

book1 = Book(author='Conan Doyle', title='THE MEMOIRS OF SHERLOCK HOLMES', year=1894, genre='detective')
book2 = Book(author='Stephen King', title="BAG OF BONES", year=1998, genre='fantasy')

resume1 = Resume(resume_cd)
resume2 = Resume(resume_sk)

print(book1, resume1, sep='\n\n')
print(' * '*20)
print()
print(book2, resume2, sep='\n\n')
