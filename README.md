# riderent
Я создала в postgres базу velobike с расширением postgis
 Из архива я создала два sql файла
 shp2pgsql C:\test_shp_data\points.shp > points.sql
 shp2pgsql C:\test_shp_data\adm.shp > adm.sql
 А потом загрузила их в базу командами
 psql -h localhost -p 5434 -d velobike -U postgres -f points.sql
 psql -h localhost -p 5434 -d velobike -U postgres -f adm.sql
