import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のSurface
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_image = pg.image.load("fig/3.png")
    kk_image = pg.transform.flip(kk_image,True,False)
    kk_rct = kk_image.get_rect() #Rect取得
    kk_rct.center = 300,200   #centerに初期座標設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #キーの押下状態の取得
        p,q=0,0
        if key_lst[pg.K_UP]:
            p,q=-1,-1
        elif key_lst[pg.K_DOWN]:
            p,q=-1,1
        elif key_lst[pg.K_LEFT]:
            p,q=-1,0
        elif key_lst[pg.K_RIGHT]:
            p,q=1,0
        else:
            p,q=-1,0
        kk_rct.move_ip((p,q))
        x=tmr%3200
        # screen.blit(kk_image, [300, 200])
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_image,kk_rct) #Rect blit
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()