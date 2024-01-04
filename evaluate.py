from datasets.datasets import labels

# data = {
#     "image1_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.02818889357149601,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.021125152707099915,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.35243695974349976,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.0061037917621433735,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 9.292598406318575e-05,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.14567002654075623,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.20672279596328735,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.22624258697032928,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 0.003378557739779353,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.010038279928267002,
#     },
#     "image2_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.004645568784326315,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.9452922940254211,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.007792338728904724,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.03477640450000763,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.0008631630917079747,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.00020722750923596323,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.0003631438303273171,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.005364955402910709,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 6.690812006127089e-05,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.0006278501241467893,
#     },
#     "image3_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.021581053733825684,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.01659560017287731,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.8887230753898621,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.004165110643953085,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.00043595462921075523,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.040136564522981644,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.014306494034826756,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.003938636742532253,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 0.0006693750619888306,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.009448190219700336,
#     },
#     "image4_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.00022874808928463608,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.9982901215553284,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 2.8778347768820822e-05,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.00032704585464671254,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.0009856575634330511,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 2.2405227355193347e-05,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 8.818502124086081e-07,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 2.5565082978573628e-05,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 6.948640657356009e-05,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 2.1462503354996443e-05,
#     },
#     "image5_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.0013705375604331493,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.10292898863554001,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.00033993134275078773,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.00013892351125832647,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.8911623358726501,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.0019951972644776106,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 4.4115199671068694e-06,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.000651647278573364,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 0.0003167481336276978,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.00109130481723696,
#     },
#     "image6_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.18769468367099762,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.1332509070634842,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.010161319747567177,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.004251161590218544,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.012234970927238464,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.39956656098365784,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.0692896619439125,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.1646578311920166,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 0.005123494658619165,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.013769482262432575,
#     },
#     "image7_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.0005139955901540816,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.0033047543838620186,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.0073831817135214806,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.08069761097431183,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 5.3241936257109046e-05,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.0017703352496027946,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.8841173648834229,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.001449025934562087,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 7.078838734742021e-06,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.020703407004475594,
#     },
#     "image8_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 7.695390195294749e-06,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.00010362931061536074,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 5.784166933153756e-05,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 1.4835841284366325e-05,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 3.9051541534718126e-05,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.0005480385734699667,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.09664313495159149,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.901671290397644,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 8.844282092468347e-06,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.0009055650443769991,
#     },
#     "image9_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.001765664666891098,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.002110027940943837,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.0029608909972012043,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.0034630587324500084,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 0.0052731712348759174,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.024767015129327774,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.18189682066440582,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.6482531428337097,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 0.0019292458891868591,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.1275809407234192,
#     },
#     "image10_score": {
#         "A tranquil bedroom boasts a lush cream color scheme, elegant full-length wainscoting, and a tripartite window with serene hillside views.": 0.0018969698576256633,
#         "An ornate bedroom radiates old-world charm with polished mahogany furnishings, open wooden ceiling beams, and warm stucco wall finishes.": 0.0013708769110962749,
#         "A sophisticated bedroom space offers a cool gray color theme, decorative circular mirrors above the nightstands, and expansive mountain views from a wide window.": 0.530261218547821,
#         "An airy bedroom features romantic white bed drapery, dark wooden contrasting overhead beams, and smooth light-hued wall textures.": 0.00026752750272862613,
#         "A cozy bedroom space is adorned with intricate blue floral wallpaper, heirloom wooden furniture, and a colorful handcrafted quilt on the bed.": 2.2707003154209815e-05,
#         "A modish bedroom displays prominent gray-striped wallpaper, a sleek wall-mounted fireplace, and elegant hanging glass lighting fixtures.": 0.007902111858129501,
#         "An avant-garde loft bedroom showcases edgy black vertical dividers, polished wood surfaces, and an open-plan ensuite bathroom with minimalistic fixtures.": 0.252675324678421,
#         "An inviting artistic corner contains bold abstract paintings, a blonde wooden minimalist bed frame, and honey-colored hardwood floors.": 0.007836909033358097,
#         "A bold bedroom with a striking red and black damask wall, a sophisticated gray upholstered headboard, and a cozy reading nook in deep gray.": 2.5476638256805018e-05,
#         "A bright metropolitan bedroom features extensive glass windows with scenic city views, a fuss-free modern design, and a restrained color palette complemented by plush bedding.": 0.19774092733860016,
#     },
# }


# 以下はデータを事前に加工するか否かのコード
# 今の所そのまま直のデータを扱う方針
# for key in data.keys():
#     data[key] = {k: v * 1000 for k, v in data[key].items()}
# for key in data.keys():
#     data[key] = {k: int(v) for k, v in data[key].items()}
def calculate_f1_scores(data):
    f1_scores = []
    for j in range(len(data)):
        # for label in data["image" + str(j + 1) + "_score"].keys():
        p_jj = data["image" + str(j + 1) + "_score"][labels[j]]
        sum_i = sum(
            data["image" + str(i + 1) + "_score"][labels[j]] for i in range(len(data))
        )
        precision = p_jj / sum_i if sum_i != 0 else 0
        recall = p_jj
        print(recall)
        if precision + recall != 0:
            f1_scores.append((2 * precision * recall) / (precision + recall))
    print(f1_scores)
    return f1_scores
