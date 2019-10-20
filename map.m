lat0 = 51.50487; 
lon0 = .05235; 
res=[0, 0, 0, 0, 0, 10, 20, 20, 20, 0, 0, 0, 20, 20, 40, 30, 40, 60, 0, 20, 20, 20, 10, 10, 20, 20, 10, 20, 20, 20, 0, 20, 20, 0, 0, 0, 0, 10, 10, 20, 20, 20, 0, 0, 0, 30, 100, 100, 100, 90, 30, 100, 30, 20, 10, 30, 10, 20, 20, 0, 0, 20, 0, 20, 20, 0, 0, 0, 0, 0, 50, 20, 10, 20, 10, 0, 0, 0, 0, 20, 10, 40, 60, 40, 40, 80, 100, 80, 20, 20, 20, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 20, 40, 10, 10, 20, 20, 0, 0, 30, 30, 20, 40, 70, 30, 60, 10, 20, 100, 40, 70, 90, 80, 70, 50, 20, 10, 10, 0, 20, 20, 0, 0, 0, 10, 10, 20, 10, 10, 10, 10, 20, 10, 0, 0, 0, 30, 10, 20, 40, 20, 30, 30, 20, 40, 10, 20, 10, 10, 10, 20, 10, 20, 20, 10, 10, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 10, 20, 20, 10, 20, 10, 10, 40, 30, 30, 20, 10, 20, 10, 10, 10, 10, 10, 20, 10, 20, 10, 10, 10, 20, 10, 10, 10, 10, 10, 10, 10, 20, 10, 10, 10, 10, 10, 20, 30, 10, 10, 10, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 30, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 0];
radius = 100000; 
az = []; 
e = wgs84Ellipsoid;
i=1;

for lat0=(-90:10:90)
    for lon0=(-180:10:180)
        if res(i)>=80
            [lat, lon] = scircle1(lat0, lon0, radius, az, e);
            wmline(lat, lon, 'Color', 'red', 'OverlayName', '1000 Meters');
        else if res(i)
        end
        i=i+1;
    end
end