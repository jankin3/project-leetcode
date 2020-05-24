class Solution:
    def corpFlightBookings(self, bookings, n):
        change = []
        for i in range(n):
            change.append(0)

        for item in bookings:
            change[item[0] - 1] += item[2]
            if item[1] <= n - 1:
                change[item[1]] -= item[2]
        print(change)
        in_booking = []
        for i, c in enumerate(change):
            if i == 0:
                in_booking.append(c)
            else:
                in_booking.append(c+in_booking[-1])
        return in_booking


s = Solution()
bookings = [[3,3,5],[1,3,20],[1,2,15]]
n = 3
r = s.corpFlightBookings(bookings, n)
print(r)
