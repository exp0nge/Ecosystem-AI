import multiprocessing
from world.herbivore import Herbivore
from world.world import World

if __name__ == "__main__":
    inst = World(32, 32)
    herb = Herbivore(inst)
    pool = multiprocessing.Pool(multiprocessing.cpu_count() - 1)
    for i in range(0, 5):
        pool.apply_async(inst.maintain_plants())
        pool.apply_async(herb.move())
        inst.print_map()
    pool.close()
    pool.join()



