#!/usr/bin/env python
# coding: utf-8
import torch
import glob

checkpoint_path = glob.glob("/lium/raid01_b/tgranjon/dv3/tiers/checkpoints/average/*.pth")

def load(checkpoint_path):
    checkpoint = torch.load(checkpoint_path, map_location=lambda storage, loc:storage)
    return checkpoint

checkpoints = []
for path in checkpoint_path:
    print(path)
    checkpoints.append(load(path))
average = load("/lium/raid01_b/tgranjon/dv3/tiers/checkpoints/checkpoint_step000045000.pth")
print("Starting average")
for key in average["state_dict"].keys():
    check_key = []
    for checkpoint in checkpoints:
        check_key.append(checkpoint["state_dict"][key])
    average["state_dict"][key] = sum(check_key)
    average["state_dict"][key] = average["state_dict"][key] / len(check_key)
torch.save(average, "average.pth")
