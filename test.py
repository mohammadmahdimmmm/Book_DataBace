import sqlite3
import model
import LibraryDataAdapter

p1 = model.Publisher(None,"ali","tehran","https://www.harpercollins.com/")
p2 = LibraryDataAdapter.PublisherDataAdapter.insert(p1)