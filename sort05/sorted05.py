#!/usr/bin/env python3
# sorted05.py
# Micah Raabe

# Lab 73 - Sort Stability and Complex Sorts

company_gear = [('cisco', '2015', '192.168.10.14'), ('cisco', '2011', '192.168.11.14'), ('cisco', '1999', '10.10.10.14'), ('cisco', '2018', '10.1.6.14'), ('juniper', '2018', '10.7.6.10'), ('dell', '2007', '10.55.2.12'), ('juniper', '2014', '192.168.30.44'), ('cisco', '2008', '10.0.2.1'), ('cisco', '2009', '10.2.3.77'), ('dell', '2009', '10.6.77.1'), ('juniper', '2004', '192.168.66.19'), ('arista', '2016', '192.168.88.22'), ('arista', '2016', '192.68.88.11'), ('cisco', '2001', '10.12.1.7'), ('juniper', '2002', '10.0.0.2')]
def byName(x):
    return x[0]
def byYear(y):
    return y[1]
def byYearHiLow(y):
    return y[1]
def byIpLowHigh(y):
    return y[2]
vendor_name_cg = sorted(company_gear, key=byName)
vendor_name_year_cg = sorted(vendor_name_cg, key=byYear)
vendor_year_high_low = sorted(sorted(vendor_name_cg, key=byYear, reverse=True), key=byName)
vendor_ip_low_high = sorted(sorted(vendor_name_cg, key=byIpLowHigh), key=byName)
print('\nThe list company_gear looks like: ', company_gear)
print('\nResult of sorted(company_gear, key=byUserName): ' + str(vendor_name_cg))
print('\nResult of sorted(vendor_name_cg, key=byYear): ' + str(vendor_name_year_cg))
print('\nResult of sorted(by name and year, reverse=True): ' + str(vendor_year_high_low))
print('\nResult of sorted(by name and IP): ' + str(vendor_ip_low_high))
