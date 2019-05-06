## Log Analysis

#### The data
To download the data use next link in the terminal
```
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```
This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons.

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

```
    psql -d news
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Running the file
Python3 in included in vagrant
run the following command in the terminal
```
python3 catalog/log.py
```