import random

raw_point_color = (0.7, 0.7, 0.7)
centroid_color = (0, 0, 1)
base_colors = [(1, 0, 0), (0, 1, 0), (0.5, 0, 0.5), (1, 0.5, 0)]


def generate_contrast_colors(num_colors, threshold=0.3):
    colors = base_colors[:num_colors]  # Возьмем первые пять цветов, если нужно
    num_to_generate = num_colors - len(colors)

    for _ in range(num_to_generate):
        while True:
            hue = random.uniform(0, 1)  # Случайное значение оттенка
            saturation = random.uniform(0.6, 1.0)  # Случайная насыщенность (чтобы избежать слишком бледных цветов)
            value = random.uniform(0.6, 1.0)  # Случайное значение яркости (чтобы избежать слишком темных цветов)
            rgb_color = hsv_to_rgb(hue, saturation, value)

            # Проверка на схожесть с уже сгенерированными цветами
            similar = False
            for existing_color in colors:
                if color_distance(rgb_color, existing_color) < threshold:
                    similar = True
                    break

            if not similar:
                colors.append(rgb_color)
                break

    return colors


def hsv_to_rgb(h, s, v):
    if s == 0:
        r = g = b = v
    else:
        h *= 6.0
        i = int(h)
        f = h - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        if i == 0:
            r, g, b = v, t, p
        elif i == 1:
            r, g, b = q, v, p
        elif i == 2:
            r, g, b = p, v, t
        elif i == 3:
            r, g, b = p, q, v
        elif i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q
    return (r, g, b)


def color_distance(color1, color2):
    # Вычисление "расстояния" между цветами
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
