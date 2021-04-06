docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest -p 8080:8080 -v /usr/local/var:/var/lib/mysql
