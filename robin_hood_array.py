from manim import *

class RobinHoodInsertion(Scene):

    def construct(self):
        #  0) TITLE SLIDE 
        title1 = Text("Robin Hood Addressing", font_size=48, color=WHITE)
        title2 = Text("Insertion & Deletion Process", font_size=36, color=WHITE).next_to(title1, DOWN, buff=0.5)
        title3 = Text("Presented by Sagnik Das", font_size=28, color=YELLOW).next_to(title2, DOWN, buff=0.5)
        titles = VGroup(title1, title2, title3)
        titles.move_to(UP * 1.0)
        self.play(FadeIn(titles), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(titles), run_time=0.8)
        self.wait(0.3)

        #  1) SMALL HEADER ─
        header_title = Text("Robin Hood Addressing", font_size=36, color=BLUE)
        header_text = Text(
            "When we insert an element, if the element we’re inserting is\n"
            "further from home than the current element, we displace that\n"
            "element to make room for the new one.",
            font_size=20,
            line_spacing=0.4,
            color=WHITE
        )
        header = VGroup(header_title, header_text)
        header.arrange(DOWN, buff=0.2)
        header.move_to(UP * 3.0)
        self.play(Write(header_title), Write(header_text), run_time=1.0)
        self.wait(1.0)

        #  2) ARRAY SLOTS (indices 4..13) 
        n_slots = 10  # showing indices 4 through 13
        slot_width = 0.8
        array_y = -1.5  # move array just below center
        total_width = n_slots * slot_width
        leftmost = -total_width / 2 + slot_width / 2

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

            lbl = Text(str(idx), font_size=18, color=WHITE)
            lbl.next_to(center, DOWN, buff=0.2)
            slot_labels.add(lbl)

        self.play(Create(slot_rects), Write(slot_labels), run_time=1.0)
        self.wait(0.8)

        #  3) PENDING KEYS DISPLAYED JUST ABOVE ARRAY ─
        pending_texts = ["A(5)", "B(5)", "C(5)", "D(8)", "E(7)", "F(6)", "G(5)"]
        pending_keys = []  # list of Text mobjects
        start_x = -total_width / 4
        for j, text in enumerate(pending_texts):
            pos = [start_x + j * slot_width * 1.2, array_y + 1.2, 0]
            key_mob = Text(text, font_size=22, color=WHITE).move_to(pos)
            pending_keys.append(key_mob)
            self.add(key_mob)

        self.wait(0.8)

        # Keep a dict of occupied slots: index -> mobject
        occupied = {}

        # Helper to show notification (1.5 seconds) at bottom
        def show_notification(msg):
            wrapped = msg.replace(". ", ".\n")
            note = Text(
                wrapped,
                font_size=18,
                color=YELLOW,
                line_spacing=0.3
            )
            note.to_edge(DOWN).shift(UP * 0.5)
            box = SurroundingRectangle(note, color=YELLOW, buff=0.15)
            grp = VGroup(box, note)
            self.play(FadeIn(grp), run_time=0.3)
            self.wait(2)
            self.play(FadeOut(grp), run_time=0.3)

        #  STEP 1: Insert A(5) into index 5 
        a_key = pending_keys.pop(0)  # "A(5)"
        self.play(a_key.animate.scale(1.1), run_time=0.2)
        target = slot_centers[5 - 4]  # index 5 → slot 1
        self.play(a_key.animate.move_to([target[0], target[1] + 0.6, 0]), run_time=0.4)
        a_permanent = Text("A(5)", font_size=22, color=PINK).move_to(target)
        self.play(FadeOut(a_key), Create(a_permanent), run_time=0.4)
        occupied[5] = a_permanent
        self.wait(1)

        #  STEP 2: Insert B(5) → hover 5 then place at 6 ─
        b_key = pending_keys.pop(0)
        self.play(b_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(b_key.animate.move_to([hover5[0], hover5[1] + 0.6, 0]), run_time=0.4)
        target6 = slot_centers[6 - 4]
        self.play(b_key.animate.move_to([target6[0], target6[1] + 0.6, 0]), run_time=0.4)
        b_permanent = Text("B(5)", font_size=22, color=BLUE_E).move_to(target6)
        self.play(FadeOut(b_key), Create(b_permanent), run_time=0.4)
        occupied[6] = b_permanent
        self.wait(1)

        #  STEP 3: Insert C(5) → hover5→hover6→place7 ─
        c_key = pending_keys.pop(0)
        self.play(c_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(c_key.animate.move_to([hover5[0], hover5[1] + 0.6, 0]), run_time=0.3)
        hover6 = slot_centers[6 - 4]
        self.play(c_key.animate.move_to([hover6[0], hover6[1] + 0.6, 0]), run_time=0.3)
        target7 = slot_centers[7 - 4]
        self.play(c_key.animate.move_to([target7[0], target7[1] + 0.6, 0]), run_time=0.3)
        c_permanent = Text("C(5)", font_size=22, color=GREEN).move_to(target7)
        self.play(FadeOut(c_key), Create(c_permanent), run_time=0.3)
        occupied[7] = c_permanent
        self.wait(1)

        #  STEP 4: Insert D(8) directly at index 8 
        d_key = pending_keys.pop(0)
        self.play(d_key.animate.scale(1.1), run_time=0.2)
        target8 = slot_centers[8 - 4]
        self.play(d_key.animate.move_to([target8[0], target8[1] + 0.6, 0]), run_time=0.4)
        d_permanent = Text("D(8)", font_size=22, color=ORANGE).move_to(target8)
        self.play(FadeOut(d_key), Create(d_permanent), run_time=0.4)
        occupied[8] = d_permanent
        self.wait(1)

        #  STEP 5: Insert E(7) → hover7→hover8→steal D→place E@8, D@9 
        e_key = pending_keys.pop(0)
        self.play(e_key.animate.scale(1.1), run_time=0.2)
        hover7 = slot_centers[7 - 4]
        self.play(e_key.animate.move_to([hover7[0], hover7[1] + 0.6, 0]), run_time=0.3)
        hover8 = slot_centers[8 - 4]
        self.play(e_key.animate.move_to([hover8[0], hover8[1] + 0.6, 0]), run_time=0.3)
        show_notification("E is further from home than D.\nIt's not fair D gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        e_permanent = Text("E(7)", font_size=22, color=PURPLE_D).move_to(target8)
        self.play(Create(e_permanent), FadeOut(e_key), run_time=0.3)
        occupied[8] = e_permanent
        target9 = slot_centers[9 - 4]
        self.play(d_permanent.animate.move_to(target9), run_time=0.4)
        occupied[9] = d_permanent
        self.wait(1)

        #  STEP 6: Insert F(6) → hover6→7→8→steal E→place F@8, E@9→steal D→place E@9, D@10 ─
        f_key = pending_keys.pop(0)
        self.play(f_key.animate.scale(1.1), run_time=0.2)
        hover6 = slot_centers[6 - 4]
        self.play(f_key.animate.move_to([hover6[0], hover6[1] + 0.6, 0]), run_time=0.3)
        hover7 = slot_centers[7 - 4]
        self.play(f_key.animate.move_to([hover7[0], hover7[1] + 0.6, 0]), run_time=0.3)
        hover8 = slot_centers[8 - 4]
        self.play(f_key.animate.move_to([hover8[0], hover8[1] + 0.6, 0]), run_time=0.3)
        show_notification("F is further from home than E.\nIt's not fair that E gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        f_permanent = Text("F(6)", font_size=22, color=GOLD).move_to(target8)
        self.play(Create(f_permanent), FadeOut(f_key), run_time=0.3)
        occupied[8] = f_permanent
        target9 = slot_centers[9 - 4]
        self.play(e_permanent.animate.move_to([target9[0], target9[1] + 0.6, 0]), run_time=0.4)
        show_notification("E is further from home than D.\nIt's not fair that D gets this slot.")
        self.play(FadeOut(occupied[9]), run_time=0.3)
        e_permanent.move_to(target9)
        self.play(Create(e_permanent), run_time=0.3)
        occupied[9] = e_permanent
        target10 = slot_centers[10 - 4]
        self.play(d_permanent.animate.move_to(target10), run_time=0.4)
        occupied[10] = d_permanent
        self.wait(1)

        #  STEP 7: Insert G(5) → hover5→6→7→8→steal F→place G@8, F@9→steal E→place F@9, E@10→steal D→place E@10, D@11 ─
        g_key = pending_keys.pop(0)
        self.play(g_key.animate.scale(1.1), run_time=0.2)
        hover5 = slot_centers[5 - 4]
        self.play(g_key.animate.move_to([hover5[0], hover5[1] + 0.6, 0]), run_time=0.2)
        hover6 = slot_centers[6 - 4]
        self.play(g_key.animate.move_to([hover6[0], hover6[1] + 0.6, 0]), run_time=0.2)
        hover7 = slot_centers[7 - 4]
        self.play(g_key.animate.move_to([hover7[0], hover7[1] + 0.6, 0]), run_time=0.2)
        hover8 = slot_centers[8 - 4]
        self.play(g_key.animate.move_to([hover8[0], hover8[1] + 0.6, 0]), run_time=0.2)
        show_notification("G is further from home than F.\nIt's not fair that F gets this slot.")
        self.play(FadeOut(occupied[8]), run_time=0.3)
        g_permanent = Text("G(5)", font_size=22, color=TEAL).move_to(target8)
        self.play(Create(g_permanent), FadeOut(g_key), run_time=0.3)
        occupied[8] = g_permanent
        target9 = slot_centers[9 - 4]
        self.play(f_permanent.animate.move_to([target9[0], target9[1] + 0.6, 0]), run_time=0.4)
        show_notification("F is further from home than E.\nIt's not fair that E gets this slot.")
        self.play(FadeOut(occupied[9]), run_time=0.3)
        f_permanent.move_to(target9)
        self.play(Create(f_permanent), run_time=0.3)
        occupied[9] = f_permanent
        target10 = slot_centers[10 - 4]
        self.play(e_permanent.animate.move_to([target10[0], target10[1] + 0.6, 0]), run_time=0.4)
        show_notification("E is further from home than D.\nIt's not fair that D gets this slot.")
        self.play(FadeOut(occupied[10]), run_time=0.3)
        e_permanent.move_to(target10)
        self.play(Create(e_permanent), run_time=0.3)
        occupied[10] = e_permanent
        target11 = slot_centers[11 - 4]
        self.play(d_permanent.animate.move_to(target11), run_time=0.4)
        occupied[11] = d_permanent
        self.wait(1)

        #  FINAL END 
        self.wait(2.0)

class RobinHoodDeletion(Scene):
    """
    Manual, step‐by‐step Robin Hood hashing deletion (indices 4..13).
    We begin with the array fully populated (as after insertion), then delete F(6)
    at index 9 and “pull back” E, D, H in turn until we reach H’s home slot.
    """

    def construct(self):
        #  1) HEADER (same style as insertion) 
        header_title = Text("Robin Hood Addressing", font_size=36, color=BLUE)
        header_text = Text(
            "When we delete an element, we must fill its slot by\n"
            "pulling each subsequent key closer to its home until\n"
            "we reach one that is already home.",
            font_size=20,
            line_spacing=0.4,
            color=WHITE
        )
        header = VGroup(header_title, header_text)
        header.arrange(DOWN, buff=0.2)
        header.move_to(UP * 3.0)
        self.play(Write(header_title), Write(header_text), run_time=1.0)
        self.wait(1.0)

        #  2) DRAW ARRAY SLOTS (indices 4..13) ─
        n_slots = 10           # showing slots 4..13
        slot_width = 0.8
        array_y = -1.5         # push array down slightly
        total_width = n_slots * slot_width
        leftmost = -total_width / 2 + slot_width / 2

        slot_centers = []
        slot_rects = VGroup()
        slot_indices = VGroup()
        for i in range(n_slots):
            idx = 4 + i
            center = np.array([leftmost + i * slot_width, array_y, 0])
            slot_centers.append(center)

            rect = Rectangle(width=slot_width, height=slot_width, color=WHITE, stroke_width=2)
            rect.move_to(center)
            slot_rects.add(rect)

            lbl = Text(str(idx), font_size=18, color=WHITE)
            lbl.next_to(center, DOWN, buff=0.2)
            slot_indices.add(lbl)

        self.play(Create(slot_rects), Write(slot_indices), run_time=1.0)
        self.wait(1.0)

        #  3) PLACE “PERMANENT” KEYS AT THEIR SLOTS 
        #  Initial state (after insertion):
        #    index 5 → A(5) (PINK)
        #    index 6 → B(5) (BLUE_E)
        #    index 7 → C(5) (GREEN)
        #    index 8 → G(5) (TEAL)
        #    index 9 → F(6) (GOLD)    ← We will delete this
        #    index 10 → E(7) (PURPLE_D)
        #    index 11 → D(8) (ORANGE)
        #    index 12 → H(12) (WHITE)
        #    index 13 → I(13) (WHITE)

        a_mob = Text("A(5)", font_size=22, color=PINK).move_to(slot_centers[5 - 4])
        b_mob = Text("B(5)", font_size=22, color=BLUE_E).move_to(slot_centers[6 - 4])
        c_mob = Text("C(5)", font_size=22, color=GREEN).move_to(slot_centers[7 - 4])
        g_mob = Text("G(5)", font_size=22, color=TEAL).move_to(slot_centers[8 - 4])
        f_mob = Text("F(6)", font_size=22, color=GOLD).move_to(slot_centers[9 - 4])
        e_mob = Text("E(7)", font_size=22, color=PURPLE_D).move_to(slot_centers[10 - 4])
        d_mob = Text("D(8)", font_size=22, color=ORANGE).move_to(slot_centers[11 - 4])
        h_mob = Text("H(12)", font_size=22, color=WHITE).move_to(slot_centers[12 - 4])
        i_mob = Text("I(13)", font_size=22, color=WHITE).move_to(slot_centers[13 - 4])

        occupied = {
            5: a_mob,
            6: b_mob,
            7: c_mob,
            8: g_mob,
            9: f_mob,
            10: e_mob,
            11: d_mob,
            12: h_mob,
            13: i_mob,
        }

        # Fade in all existing keys simultaneously
        self.play(
            Create(a_mob),
            Create(b_mob),
            Create(c_mob),
            Create(g_mob),
            Create(f_mob),
            Create(e_mob),
            Create(d_mob),
            Create(h_mob),
            Create(i_mob),
            run_time=1.0
        )
        self.wait(0.8)

        #  4) HELPER: “SHOW NOTIFICATION BOX” 
        def show_notification(msg, position=UP * 0.5):
            # Wrap at the “. ” boundary
            wrapped = msg.replace(". ", ".\n")
            note = Text(wrapped, font_size=18, color=YELLOW, line_spacing=0.3)
            note.move_to(position)

            box = SurroundingRectangle(note, color=YELLOW, buff=0.15)
            grp = VGroup(box, note)
            self.play(FadeIn(grp), run_time=0.3)
            self.wait(1.5)
            self.play(FadeOut(grp), run_time=0.3)

        #  5) STEP 1: DELETE F(6) at index 9 
        #   Fade out F(6); leave slot 9 empty
        self.play(FadeOut(f_mob), run_time=0.4)
        occupied.pop(9)
        self.wait(1.0)

        # Show message: “We can’t leave this slot blank. How should we fill it?”
        # We’ll point to slot 9
        msg1 = "We can’t leave this slot blank.\nHow should we fill it?"
        box1 = Text("We can’t leave this slot blank.\nHow should we fill it?", font_size=20, color=WHITE)
        # Place message slightly above the array (centered)
        box1.move_to(UP * 0.5)
        arrow1 = Arrow(
            start=box1.get_bottom() + 0.1 * DOWN,
            end=slot_centers[9 - 4] + 0.2 * UP,
            color=BLUE,
            buff=0
        )
        self.play(FadeIn(box1), Create(arrow1), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(box1), FadeOut(arrow1), run_time=0.3)
        self.wait(0.6)

        #  6) STEP 2: “PULL BACK” E(7) from index 10 to fill index 9 ─
        # Show notification arrow from E’s home‐distance context:
        msg2 = "This element is far from home.\nLet’s move it closer!"
        box2 = Text(msg2, font_size=20, color=WHITE)
        box2.move_to(UP * 0.5)
        arrow2 = Arrow(
            start=box2.get_bottom() + 0.1 * DOWN,
            end=slot_centers[10 - 4] + 0.2 * UP,
            color=BLUE,
            buff=0
        )
        self.play(FadeIn(box2), Create(arrow2), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(box2), FadeOut(arrow2), run_time=0.3)
        self.wait(0.6)

        # Animate: E from slot 10 → slot 9
        self.play(e_mob.animate.move_to(slot_centers[9 - 4]), run_time=0.5)
        occupied[9] = e_mob
        occupied.pop(10)
        self.wait(0.8)

        #  7) STEP 3: “PULL BACK” D(8) from index 11 → index 10 ─
        msg3 = "This element is far from home.\nLet’s move it closer!"
        box3 = Text(msg3, font_size=20, color=WHITE)
        box3.move_to(UP * 0.5)
        arrow3 = Arrow(
            start=box3.get_bottom() + 0.1 * DOWN,
            end=slot_centers[11 - 4] + 0.2 * UP,
            color=BLUE,
            buff=0
        )
        self.play(FadeIn(box3), Create(arrow3), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(box3), FadeOut(arrow3), run_time=0.3)
        self.wait(0.6)

        # Animate: D from slot 11 → slot 10
        self.play(d_mob.animate.move_to(slot_centers[10 - 4]), run_time=0.5)
        occupied[10] = d_mob
        occupied.pop(11)
        self.wait(0.6)

        #  8) STEP 4: “CHECK” H(12) at index 12 ─
        # Because H’s home is 12, it does not move. Show a final message.
        msg4 = "This element is already home.\nWe’re done."
        box4 = Text(msg4, font_size=20, color=WHITE)
        box4.move_to(UP * 0.5)
        arrow4 = Arrow(
            start=box4.get_bottom() + 0.1 * DOWN,
            end=slot_centers[12 - 4] + 0.2 * UP,  # pointing to index 11 (just vacated)
            color=BLUE,
            buff=0
        )
        # Actually, we want to point at H’s slot 12 to show it stays in place:
        arrow4_end = slot_centers[12 - 4] + 0.2 * UP
        arrow4 = Arrow(start=box4.get_bottom() + 0.1 * DOWN, end=arrow4_end, color=BLUE, buff=0)
        self.play(FadeIn(box4), Create(arrow4), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(box4), FadeOut(arrow4), run_time=0.3)
        self.wait(0.6)

        #  9) FINAL PAUSE 
        self.wait(2.0)