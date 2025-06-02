from manim import *

class RobinHoodArrayAnimationManual(Scene):
    """
    Manual step-by-step Robin Hood hashing insertion (indices 4..13), without loops.
    """

    def construct(self):
        #  1) HEADER 
        header = Text(
            "Robin Hood hashing is a slight modification to linear probing. "
            "When inserting, if the new element is further from its home than its occupant, we displace that occupant.",
            font_size=24,
            line_spacing=0.4
        )
        header.to_edge(UP).shift(DOWN * 1.0)
        self.play(Write(header), run_time=1.0)
        self.wait(0.5)

        #  2) ARRAY SLOTS (indices 4..13) 
        n_slots = 10  # showing indices 4 through 13
        slot_width = 0.8
        array_y = -1.0
        total_width = n_slots * slot_width
        leftmost = -total_width/2 + slot_width/2
        slot_centers = []
        slot_rects = VGroup()
        slot_labels = VGroup()
        for i in range(n_slots):
            idx = 4 + i
            center = [leftmost + i * slot_width, array_y, 0]
            slot_centers.append(center)
            rect = Rectangle(width=slot_width, height=slot_width, color=WHITE, stroke_width=2)
            rect.move_to(center)
            slot_rects.add(rect)
            lbl = Text(str(idx), font_size=20, color=WHITE)
            lbl.next_to(center, DOWN, buff=0.2)
            slot_labels.add(lbl)
        self.play(Create(slot_rects), Write(slot_labels), run_time=1.0)
        self.wait(0.5)

        #  3) PENDING KEYS DISPLAYED ABOVE ARRAY 
        pending_texts = ["A(5)", "B(5)", "C(5)", "D(8)", "E(7)", "F(6)", "G(5)"]
        pending_positions = []
        pending_keys = []  # list of mobjects
        start_x = -total_width/4
        for j, text in enumerate(pending_texts):
            pos = [start_x + j * slot_width * 1.2, array_y + 1.5, 0]
            key_mob = Text(text, font_size=24, color=WHITE).move_to(pos)
            pending_keys.append(key_mob)
            self.add(key_mob)
        self.wait(0.5)

        # Keep a dict of occupied slots: index -> mobject
        occupied = {}

        # Helper to show notification
        def show_notification(msg):
            note = Text(msg, font_size=20, color=YELLOW).to_edge(UP).shift(DOWN * 1.5)
            box = SurroundingRectangle(note, color=YELLOW, buff=0.2)
            grp = VGroup(box, note)
            self.play(FadeIn(grp), run_time=0.3)
            self.wait(1.5)
            self.play(FadeOut(grp), run_time=0.3)

        #  STEP 1: Insert A(5) into index 5 
        a_key = pending_keys.pop(0)  # "A(5)"
        self.play(a_key.animate.scale(1.1), run_time=0.2)
        target = slot_centers[5 - 4]  # slot for index 5 is array slot 1
        self.play(a_key.animate.move_to([target[0], target[1]+0.5, 0]), run_time=0.4)
        a_permanent = Text("A(5)", font_size=24, color=PINK).move_to(target)
        self.play(FadeOut(a_key), Create(a_permanent), run_time=0.4)
        occupied[5] = a_permanent
        self.wait(0.5)

        #  STEP 2: Insert B(5) → hover 5 then place at 6 
        b_key = pending_keys.pop(0)
        self.play(b_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(b_key.animate.move_to([hover5[0], hover5[1]+0.5, 0]), run_time=0.4)
        target6 = slot_centers[6 - 4]
        self.play(b_key.animate.move_to([target6[0], target6[1]+0.5, 0]), run_time=0.4)
        b_permanent = Text("B(5)", font_size=24, color=BLUE_E).move_to(target6)
        self.play(FadeOut(b_key), Create(b_permanent), run_time=0.4)
        occupied[6] = b_permanent
        self.wait(0.5)

        #  STEP 3: Insert C(5) → hover5→hover6→place7 
        c_key = pending_keys.pop(0)
        self.play(c_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(c_key.animate.move_to([hover5[0], hover5[1]+0.5, 0]), run_time=0.3)
        hover6 = slot_centers[6 - 4]
        self.play(c_key.animate.move_to([hover6[0], hover6[1]+0.5, 0]), run_time=0.3)
        target7 = slot_centers[7 - 4]
        self.play(c_key.animate.move_to([target7[0], target7[1]+0.5, 0]), run_time=0.3)
        c_permanent = Text("C(5)", font_size=24, color=GREEN).move_to(target7)
        self.play(FadeOut(c_key), Create(c_permanent), run_time=0.3)
        occupied[7] = c_permanent
        self.wait(0.5)

        #  STEP 4: Insert D(8) directly at index 8 
        d_key = pending_keys.pop(0)
        self.play(d_key.animate.scale(1.1), run_time=0.2)
        target8 = slot_centers[8 - 4]
        self.play(d_key.animate.move_to([target8[0], target8[1]+0.5, 0]), run_time=0.4)
        d_permanent = Text("D(8)", font_size=24, color=ORANGE).move_to(target8)
        self.play(FadeOut(d_key), Create(d_permanent), run_time=0.4)
        occupied[8] = d_permanent
        self.wait(0.5)

        #  STEP 5: Insert E(7) → hover7→hover8→steal D→place E@8, D@9 
        e_key = pending_keys.pop(0)
        self.play(e_key.animate.scale(1.1), run_time=0.2)
        hover7 = slot_centers[7 - 4]
        self.play(e_key.animate.move_to([hover7[0], hover7[1]+0.5, 0]), run_time=0.3)
        hover8 = slot_centers[8 - 4]
        self.play(e_key.animate.move_to([hover8[0], hover8[1]+0.5, 0]), run_time=0.3)
        show_notification("E is further from home than D. It's not fair D gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        e_permanent = Text("E(7)", font_size=24, color=PURPLE_D).move_to(target8)
        self.play(Create(e_permanent), FadeOut(e_key), run_time=0.3)
        occupied[8] = e_permanent
        target9 = slot_centers[9 - 4]
        self.play(d_permanent.animate.move_to(target9), run_time=0.4)
        occupied[9] = d_permanent
        self.wait(0.5)

        #  STEP 6: Insert F(6) → hover6→7→8→steal E→place F@8, E@9→steal D→place E@9, D@10 
        f_key = pending_keys.pop(0)
        self.play(f_key.animate.scale(1.1), run_time=0.2)
        hover6 = slot_centers[6 - 4]
        self.play(f_key.animate.move_to([hover6[0], hover6[1]+0.5, 0]), run_time=0.3)
        hover7 = slot_centers[7 - 4]
        self.play(f_key.animate.move_to([hover7[0], hover7[1]+0.5, 0]), run_time=0.3)
        hover8 = slot_centers[8 - 4]
        self.play(f_key.animate.move_to([hover8[0], hover8[1]+0.5, 0]), run_time=0.3)
        show_notification("F is further from home than E. It's not fair that E gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        f_permanent = Text("F(6)", font_size=24, color=GOLD).move_to(target8)
        self.play(Create(f_permanent), FadeOut(f_key), run_time=0.3)
        occupied[8] = f_permanent
        target9 = slot_centers[9 - 4]
        self.play(e_permanent.animate.move_to([target9[0], target9[1]+0.5, 0]), run_time=0.4)
        show_notification("E is further from home than D. It's not fair that D gets this slot.")
        self.play(FadeOut(occupied[9]), run_time=0.3)
        e_permanent.move_to(target9)
        self.play(Create(e_permanent), run_time=0.3)
        occupied[9] = e_permanent
        target10 = slot_centers[10 - 4]
        self.play(d_permanent.animate.move_to(target10), run_time=0.4)
        occupied[10] = d_permanent
        self.wait(0.5)

        #  STEP 7: Insert G(5) → hover5→6→7→8→steal F→place G@8, F@9→steal E→place F@9, E@10→steal D→place E@10, D@11 
        g_key = pending_keys.pop(0)
        self.play(g_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(g_key.animate.move_to([hover5[0], hover5[1]+0.5, 0]), run_time=0.2)
        hover6 = slot_centers[6 - 4]
        self.play(g_key.animate.move_to([hover6[0], hover6[1]+0.5, 0]), run_time=0.2)
        hover7 = slot_centers[7 - 4]
        self.play(g_key.animate.move_to([hover7[0], hover7[1]+0.5, 0]), run_time=0.2)
        hover8 = slot_centers[8 - 4]
        self.play(g_key.animate.move_to([hover8[0], hover8[1]+0.5, 0]), run_time=0.2)
        show_notification("G is further from home than F. It's not fair that F gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        g_permanent = Text("G(5)", font_size=24, color=TEAL).move_to(target8)
        self.play(Create(g_permanent), FadeOut(g_key), run_time=0.3)
        occupied[8] = g_permanent
        target9 = slot_centers[9 - 4]
        self.play(f_permanent.animate.move_to([target9[0], target9[1]+0.5, 0]), run_time=0.4)
        show_notification("F is further from home than E. It's not fair that E gets this slot.")
        self.play(FadeOut(occupied[9]), run_time=0.3)
        f_permanent.move_to(target9)
        self.play(Create(f_permanent), run_time=0.3)
        occupied[9] = f_permanent
        target10 = slot_centers[10 - 4]
        self.play(e_permanent.animate.move_to([target10[0], target10[1]+0.5, 0]), run_time=0.4)
        show_notification("E is further from home than D. It's not fair that D gets this slot.")
        self.play(FadeOut(occupied[10]), run_time=0.3)
        e_permanent.move_to(target10)
        self.play(Create(e_permanent), run_time=0.3)
        occupied[10] = e_permanent
        target11 = slot_centers[11 - 4]
        self.play(d_permanent.animate.move_to(target11), run_time=0.4)
        occupied[11] = d_permanent
        self.wait(0.5)

        #  FINAL END 
        self.wait(1.0)