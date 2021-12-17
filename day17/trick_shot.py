import sys, math, time


def xpos_at_step(hor_vel, step):
    if step > hor_vel:
        # terminal xpos
        return (hor_vel * (hor_vel + 1)) / 2
    else:
        return (hor_vel * (hor_vel + 1)) / 2 - ((hor_vel - step) * (hor_vel - step + 1) / 2)


def ypos_at_step(ver_vel, step):
    if step <= ver_vel:
        return (ver_vel * (ver_vel + 1)) / 2 - ((ver_vel - step) * (ver_vel - step + 1) / 2)
    else:
        ymax = max_height(ver_vel)
        return ymax - ((step - ver_vel) * (step - (ver_vel + 1)) / 2)


def hor_vel_min(rect):
    x1 = rect[0][0]
    # løs som andregradslikningen x^2+x-2*x1=0, hvor x1 er input
    return math.ceil((-1 + math.sqrt(1 - (4 * -2 * x1))) / 2)


def hor_vel_max(rect):
    return rect[0][1] + 1


def max_height(ver_verl):
    return (ver_verl * (ver_verl + 1)) // 2


def hits_target(target, hor_vel, ver_vel):
    x1 = target[0][0]
    x2 = target[0][1]
    y1 = target[1][0]
    y2 = target[1][1]
    step = 1
    posx = 0
    posy = 0
    while posx <= x2 and posy >= y1:
        posx += hor_vel
        posy += ver_vel
        if x1 <= posx and x2 >= posx and y1 <= posy and y2 >= posy:
            return True
        step += 1
        if hor_vel > 0:
            hor_vel -= 1
        ver_vel -= 1
    return False


def main():
    start_time = time.time()
    input = sys.stdin.readline().strip()
    target_rect = [tuple(map(int, seg.split(".."))) for seg in input[15:].split(", y=")]
    ymax = -100000
    count = 0
    for hor_vel in range(hor_vel_min(target_rect), hor_vel_max(target_rect)):
        for ver_vel in range(-200, 200):
            if hits_target(target_rect, hor_vel, ver_vel):
                count += 1
                if max_height(ver_vel) > ymax:
                    ymax = max_height(ver_vel)
    print("velocities", count)
    print("ymax", ymax)
    print("--- %s seconds ---" % (time.time() - start_time))


main()