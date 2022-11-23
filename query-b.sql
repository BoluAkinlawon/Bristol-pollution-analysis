select readings.stationid, stations.location, readings.datetime, avg(readings.`pm2.5`) "Average PM2.5", avg(readings.`vpm2.5`) "Average VPM2.5" from readings left outer join stations on (stations.stationid = readings.stationid) where readings.datetime like '2019%' and readings.datetime like '%08:00%' group by readings.stationid;