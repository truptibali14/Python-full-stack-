Visitors=[500,1200,700,560,890,1000,5000]
highest_traffic=max(Visitors)
lowest_traffic=min(Visitors)
highest_day=Visitors.index(highest_traffic)+1
lowest_day=Visitors.index(lowest_traffic)+1
print("highest_traffic_day",highest_traffic)
print("lowest_traffic_day",lowest_traffic)
