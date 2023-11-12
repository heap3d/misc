#!/usr/bin/python
import modo
import lx


def next_key(item: modo.Item):
    item.select(replace=True)
    lx.eval('item.selectChannels anim')
    lx.eval('!time.step key next wrap:true')


def match_item(source_item: modo.Item, target_item: modo.Item):
    source_item.select(replace=True)
    target_item.select()

    lx.eval('item.match item pos')
    lx.eval('item.match item rot')
    lx.eval('item.match item scl')


def get_frame(time):
    fps = get_fps()
    return int(round(time * fps))


def get_fps():
    return modo.Scene().fps


def get_cur_frame():
    cur_time = lx.eval('select.time ?')
    return get_frame(cur_time)


def create_loc_at_cur_frame():
    frame = get_cur_frame()
    return modo.Scene().addItem(itype='locator', name='{}'.format(frame))


def get_in_frame():
    in_time = lx.eval('time.range in:?')
    return get_frame(in_time)


def get_out_frame():
    out_time = lx.eval('time.range in:?')
    return get_frame(out_time)


def main():
    selected = modo.Scene().selectedByType(itype='locator', superType=True)
    if selected.count() != 2:
        print('Incorrect number of items selected. First select the key item first, then select the target item.')
    key_item = selected[0]
    target_item = selected[1]
    while True:
        cur_frame = get_cur_frame()
        cur_loc = create_loc_at_cur_frame()
        match_item(cur_loc, target_item)

        next_key(key_item)
        next_frame = get_cur_frame()

        if next_frame <= cur_frame:
            break


if __name__ == '__main__':
    main()
