class C:

    def test(self) -> None:
        with patch("black.out", print):
            self.assertEqual(
                unstyle(str(report)), "1 file reformatted, 1 file failed to reformat."
            )
            self.assertEqual(
                unstyle(str(report)),
                "1 file reformatted, 1 file left unchanged, 1 file failed to reformat.",
            )
            self.assertEqual(
                unstyle(str(report)),
                "2 files reformatted, 1 file left unchanged, "
                "1 file failed to reformat.",
            )
            self.assertEqual(
                unstyle(str(report)),
                "2 files reformatted, 2 files left unchanged, "
                "2 files failed to reformat.",
            )
            for i in (a,):
                if (
                    # Rule 1
                    i % 2 == 0
                    # Rule 2
                    and i % 3 == 0
                ):
                    while (
                        # Just a comment
                        call()
                        # Another
                    ):
                        print(i)

    def omitting_trailers(self) -> None:
        get_collection(
            hey_this_is_a_very_long_call, it_has_funny_attributes, really=True
        )[OneLevelIndex]
        get_collection(
            hey_this_is_a_very_long_call, it_has_funny_attributes, really=True
        )[OneLevelIndex][TwoLevelIndex][ThreeLevelIndex][FourLevelIndex]
        d[0][1][2][3][4][5][6][7][8][9][10][11][12][13][14][15][16][17][18][19][20][21][
            22
        ]

    def easy_asserts(self) -> None:
        assert {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        } == expected, "Not what we expected"

        assert expected == {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        }, "Not what we expected"

        assert expected == {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        }

    def tricky_asserts(self) -> None:
        assert {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        } == expected(
            value, is_going_to_be="too long to fit in a single line", srsly=True
        ), "Not what we expected"

        assert {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        } == expected, (
            "Not what we expected and the message is too long to fit in one line"
        )

        assert expected(
            value, is_going_to_be="too long to fit in a single line", srsly=True
        ) == {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        }, "Not what we expected"

        assert expected == {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        }, (
            "Not what we expected and the message is too long to fit "
            "in one line because it's too long"
        )

        # This is weird but true.
        assert expectedexpectedexpectedexpectedexpectedexpectedexpectedexpectedexpect == {
            key1: value1,
            key2: value2,
            key3: value3,
            key4: value4,
            key5: value5,
            key6: value6,
            key7: value7,
            key8: value8,
            key9: value9,
        }
