# A function that blits a label onto the background of the pygame window

try:
    import pygame, sys
except ImportError:
    print("Couldn't load module")
    sys.exit()

def label(size, text, color, surface, pos):
    """A function that blits a label onto the background of the window.

    Parameters
    ----------
    size : size of the label text (int).
    text : text you want label to display (string - "example").
    color : color of the label text (enter as tuple - ex: (0, 0, 0)).
    surface : surface on which to blit the label.
    pos : x and y coordinates of the label (enter as comma-separated values).
    """

    label_font = pygame.font.SysFont("calibri", size, bold=True)
    label_text = label_font.render(text, 1, color)
    label_textpos = label_text.get_rect()
    label_textpos.centerx, label_textpos.centery = pos
    surface.blit(label_text, label_textpos)