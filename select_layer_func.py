from gimpfu import *


def select_next_layer(img, active_layer):
    select_layer(img, active_layer, True)


def select_prev_layer(img, active_layer):
    select_layer(img, active_layer, False)


# image = gimp.image_list()[0]
# layer = image.layers[0]
def select_layer(img, active_layer, next_layer):
    pdb.gimp_image_undo_freeze(img)
    layers = img.layers

    group, active_layer_idx = get_active_group_and_id(layers, active_layer)
    if group:
        layers = group.layers

    layer_id = active_layer_idx + (-1, 1)[next_layer]
    if next_layer:
        if layer_id > len(layers) - 1:
            layer_id = 0
    else:
        if layer_id < 0:
            layer_id = len(layers) - 1

    for i in range(0, len(layers)):
        layer = layers[i]
        if layer_id == i:
            layer.visible = True
            pdb.gimp_image_set_active_layer(img, layer)
        else:
            layer.visible = False

    gimp.message("selected layer " + str(layer_id))
    pdb.gimp_image_undo_thaw(img)


def get_active_group_and_id(group, active_layer):
    if type(group) == gimp.GroupLayer:
        layers = group.layers
    else:
        layers = group
    for i in range(0, len(layers)):
        layer = layers[i]
        if type(layer) == gimp.GroupLayer:
            res = get_active_group_and_id(layer, active_layer)
            if res:
                return res
        if layer == active_layer:
            if type(group) == gimp.GroupLayer:
                return [group, i]
            else:
                return [None, i]
    return False
