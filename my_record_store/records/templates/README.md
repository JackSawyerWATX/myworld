
RUN LOCALLY::

Navigate to:

    C:\Users\<myComputername>\OneDrive\Desktop\RecordStore\myworld\my_record_store

and run:

    py manage.py runserver

Open the page at:

    http://localhost:8000/

TO ADD RECORDS:

First, make sure you are in the 'my_record_store' file.
In [1]: from records.models import Record
In [2]: x = Record.objects.all()[0] <--[#] = index number-->
In [3]: x.artist = 'Artist Here'
In [4]: x.album = 'Album Title Here'
In [5]: x.record_label = 'Distributor, not Producer'
In [6]: x.released = '1996-05-25'
In [7]: x.save() <--Got it!-->
In [8]: Record.objects.all().values() <--Check You Work-->


Next to add:
    1. Cover art in the blue squares to the left of the listing.
    2. An interface to add more albums, instead of using CLI.
    3. MORE ART!