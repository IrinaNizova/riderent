# riderent
 � ������� � postgres ���� velobike � ����������� postgis
 �� ������ � ������� ��� sql �����
 shp2pgsql C:\test_shp_data\points.shp > points.sql
 shp2pgsql C:\test_shp_data\adm.shp > adm.sql
 � ����� ��������� �� � ���� ����������
 psql -h localhost -p 5434 -d velobike -U postgres -f points.sql
  psql -h localhost -p 5434 -d velobike -U postgres -f adm.sql