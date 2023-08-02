
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
In [2]: x = Record.objects.all()[0]
