import collections
def canAdd(A, m):
    A.append(m)
    A.sort()
    for i in range(len(A) - 1):
        if A[i + 1][0] < A[i][1]:
            return False
    return True


def freeTime(A):
    A.sort()
    afterMerge = []
    for s, e in A:
        if not afterMerge:
            afterMerge.append([s, e])
        else:
            if afterMerge[-1][1] >= s:
                afterMerge[-1][1] = max(afterMerge[-1][1], e)
            else:
                afterMerge.append([s, e])
    free = []
    for i in range(len(afterMerge)):
        if i == 0:
            if afterMerge[i][0] != 0:
                free.append([0, afterMerge[i][0]])
        else:
            free.append([afterMerge[i - 1][1], afterMerge[i][0]])
    return free

# print(freeTime([[1,2],[2,3],[3,4],[7,10],[2,5]]))

# meetings: [['m1', 1300, 1400, 5]] rooms:[['r1', 8]]
def distribute(meetings, rooms):
    # 1. find the overlapped meetings first then use greedy strategy to distribute rooms for overlapped meetings
    # 2. find the non-overlapped meetings to see whether the biggest room can hold all of the people
    starts = collections.defaultdict(set)
    ends = collections.defaultdict(set)
    timePoints = set()
    meetingSet = set()
    for name, s, e, n in meetings:
        starts[s].add((name, n))
        ends[e].add((name, n))
        timePoints.add(s)
        timePoints.add(e)
        meetingSet.add((name, n))
    pre = set()
    overlappedMeetings = set()
    overlapMeetingSet = [] # get overlapped meetings
    for t in sorted(list(timePoints)):
        nxt = (pre | starts[t]) - ends[t]
        if pre != nxt and len(nxt) > 1:
            overlapMeetingSet.append(list(nxt))
            overlappedMeetings |= nxt
        pre = nxt
    rooms.sort(key = lambda x : x[1])
    meeting_room = {}
    for overlapMeetings in sorted(overlapMeetingSet, key = lambda x: -len(x)):
        usedRoom = set()
        for name, n in overlapMeetings:
            if name in meeting_room: continue
            for r in rooms:
                if r[1] >= n and r[0] not in usedRoom:
                    usedRoom.add(r[0])
                    meeting_room[name] = r[0]
                    break
            if name not in meeting_room:
                print('impossible')
                return
    for nonOverlapped in meetingSet - overlappedMeetings:
        if nonOverlapped[1] > rooms[-1][1]:
            print('impossible')
            return
        meeting_room[nonOverlapped[0]] = rooms[-1][0]
    for i, j in meeting_room.items():
        print(i + ' : ' + j)


distribute([['m1', 1300, 1500, 10], ['m2', 930, 1200, 8],['m3', 830, 845, 8], ['m4',1200,1500, 9], ['m5',1200,1350, 9]], [['r1', 10], ['r2',11], ['r3', 12]])
