import matplotlib.pyplot as plt
import numpy as np
from data_formatter import format_for_visualization

zeroshot_result_data = [
    {
        "image": 1,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.6581862568855286,
    },
    {
        "image": 1,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.008602273650467396,
    },
    {
        "image": 1,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.10581830143928528,
    },
    {
        "image": 1,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.035552412271499634,
    },
    {
        "image": 1,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.0008048074087128043,
    },
    {
        "image": 1,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.01215391606092453,
    },
    {
        "image": 1,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.009663737379014492,
    },
    {
        "image": 1,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.08551564067602158,
    },
    {
        "image": 1,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.034666236490011215,
    },
    {
        "image": 1,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.04903646185994148,
    },
    {
        "image": 2,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.0016184860141947865,
    },
    {
        "image": 2,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.8691346645355225,
    },
    {
        "image": 2,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.005872984416782856,
    },
    {
        "image": 2,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.017985887825489044,
    },
    {
        "image": 2,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.0003176210157107562,
    },
    {
        "image": 2,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.0010460998164489865,
    },
    {
        "image": 2,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.0015593086136505008,
    },
    {
        "image": 2,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.10079268366098404,
    },
    {
        "image": 2,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.0014604716561734676,
    },
    {
        "image": 2,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.00021172090782783926,
    },
    {
        "image": 3,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.12905912101268768,
    },
    {
        "image": 3,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.04087064415216446,
    },
    {
        "image": 3,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.4425363838672638,
    },
    {
        "image": 3,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.01816920004785061,
    },
    {
        "image": 3,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.004566235933452845,
    },
    {
        "image": 3,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.004213366657495499,
    },
    {
        "image": 3,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.08863802999258041,
    },
    {
        "image": 3,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.12335313111543655,
    },
    {
        "image": 3,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.06677554547786713,
    },
    {
        "image": 3,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.08181838691234589,
    },
    {
        "image": 4,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.00474825082346797,
    },
    {
        "image": 4,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.04855665937066078,
    },
    {
        "image": 4,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.0003067483485210687,
    },
    {
        "image": 4,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.831041693687439,
    },
    {
        "image": 4,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.05335886776447296,
    },
    {
        "image": 4,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.04051114246249199,
    },
    {
        "image": 4,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.003827236359938979,
    },
    {
        "image": 4,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.01654687151312828,
    },
    {
        "image": 4,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.0010871067643165588,
    },
    {
        "image": 4,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 1.5434112356160767e-05,
    },
    {
        "image": 5,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.005539377219974995,
    },
    {
        "image": 5,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.005866963416337967,
    },
    {
        "image": 5,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.00020282150944694877,
    },
    {
        "image": 5,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.026761362329125404,
    },
    {
        "image": 5,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.8985271453857422,
    },
    {
        "image": 5,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.01452691201120615,
    },
    {
        "image": 5,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.004857050720602274,
    },
    {
        "image": 5,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.0028601859230548143,
    },
    {
        "image": 5,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.040787141770124435,
    },
    {
        "image": 5,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 7.102180825313553e-05,
    },
    {
        "image": 6,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.005515872500836849,
    },
    {
        "image": 6,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.020276876166462898,
    },
    {
        "image": 6,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.002311714692041278,
    },
    {
        "image": 6,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.04540949687361717,
    },
    {
        "image": 6,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.0005054700304754078,
    },
    {
        "image": 6,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.8675873875617981,
    },
    {
        "image": 6,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.00103479390963912,
    },
    {
        "image": 6,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.0035816284362226725,
    },
    {
        "image": 6,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.053306519985198975,
    },
    {
        "image": 6,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.00047033370356075466,
    },
    {
        "image": 7,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.0018202712526544929,
    },
    {
        "image": 7,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.014860325492918491,
    },
    {
        "image": 7,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.25046998262405396,
    },
    {
        "image": 7,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.21529148519039154,
    },
    {
        "image": 7,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 5.4786400141892955e-05,
    },
    {
        "image": 7,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.0007570613524876535,
    },
    {
        "image": 7,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.5130065083503723,
    },
    {
        "image": 7,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.0015544234775006771,
    },
    {
        "image": 7,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.0009856856195256114,
    },
    {
        "image": 7,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.0011993522057309747,
    },
    {
        "image": 8,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.002443143865093589,
    },
    {
        "image": 8,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.004390594083815813,
    },
    {
        "image": 8,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.001803888939321041,
    },
    {
        "image": 8,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.00021876227401662618,
    },
    {
        "image": 8,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 2.4005434170248918e-05,
    },
    {
        "image": 8,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.00024011881032492965,
    },
    {
        "image": 8,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.009996658191084862,
    },
    {
        "image": 8,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.7865504622459412,
    },
    {
        "image": 8,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.19214792549610138,
    },
    {
        "image": 8,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.0021843924187123775,
    },
    {
        "image": 9,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.007188129238784313,
    },
    {
        "image": 9,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 9.025129111250862e-05,
    },
    {
        "image": 9,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.0014233343536034226,
    },
    {
        "image": 9,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.0011113157961517572,
    },
    {
        "image": 9,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.0007587656727991998,
    },
    {
        "image": 9,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.0005364703829400241,
    },
    {
        "image": 9,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.02220095880329609,
    },
    {
        "image": 9,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.05005602538585663,
    },
    {
        "image": 9,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.9020810723304749,
    },
    {
        "image": 9,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.014553498476743698,
    },
    {
        "image": 10,
        "label": "Glass-top side table, Beige carpet runner, Square ceiling vent, Silver drawer handles, Contemporary wall sconces, Wood trim around windows, Plush white bedspread, Coordinated picture frames, Tufted upholstery on chairs, Bedside table lamps, Dual sink vanity, Flower arrangement on bedside table, Accent pillows on chairs",
        "score": 0.13281743228435516,
    },
    {
        "image": 10,
        "label": "Arched doorways, Fire burning in fireplace, Small wooden side table, Ceiling fan with light, Wood-paneled lower walls, Vaulted ceilings",
        "score": 0.014151191338896751,
    },
    {
        "image": 10,
        "label": "Stacked stone backsplash, Mounted wall mirrors, Large window with mountain view, Wood and metal staircase railing, Light switch plates, Silver drawer pulls, Decorative bed pillows, Wooden dresser with curved design, Plush throw blanket, Black metal table legs",
        "score": 0.39231735467910767,
    },
    {
        "image": 10,
        "label": "Glass-paneled windows, Wooden ceiling beams, Patterned vase, Carved wood details on furniture, Sheer curtain under drapery, White ceiling, Tassel curtain tie-backs",
        "score": 0.009301293641328812,
    },
    {
        "image": 10,
        "label": "Intricate carpet design, Brass door handle, Embroidered pillowcases, Doll on the bed, Ornate picture frames, White lace tablecloth, Traditional room decor",
        "score": 0.0006154610309749842,
    },
    {
        "image": 10,
        "label": "Classic interior architecture, Paneled walls, Diagonal wall paneling, Striped wallpaper, Warm-toned flooring, Faux fur throw, Crown molding",
        "score": 0.001585971680469811,
    },
    {
        "image": 10,
        "label": "Purple bedspread, Chrome bath filler, Square wall-mounted sink, Black curtain dividing the room, Purple flooring in bedroom area, Modern white freestanding bathtub, Light wood paneling on lower walls",
        "score": 0.09299018979072571,
    },
    {
        "image": 10,
        "label": "Recessed wall nooks, Light switches on wall, Beige fabric ottoman, Neutral-toned bedding, Orange-red color accents, Structural column in room, Art with bold colors",
        "score": 0.07603055238723755,
    },
    {
        "image": 10,
        "label": "Modern, Neutral room tones, Wall art with human figure, Patterned wallpaper accent wall, Contemporary chair, Open space under bed, Silver door handle",
        "score": 0.04948609694838524,
    },
    {
        "image": 10,
        "label": "Soft lighting ambiance, Gray upholstered bench, Neutral color palette, Nightstands with drawers, Sliding door to balcony, White walls",
        "score": 0.23070451617240906,
    },
]

data = format_for_visualization(zeroshot_result_data)
# ラベルとスコアを抽出
labels = [item["label"] for item in data]
scores_image = [[item[f"image{i+1}_score"] for i in range(10)] for item in data]

# 描画
plt.figure(figsize=(10, 6))

y = np.arange(len(labels))  # ラベルの位置
width = 0.1  # バーの幅

colors = [
    "skyblue",
    "orange",
    "green",
    "red",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "cyan",
]
for i in range(10):
    plt.barh(
        y - width * 4.5 + width * i,
        [scores[i] for scores in scores_image],
        width,
        color=colors[i],
        label=f"Image {i+1}",
    )

plt.xlabel("Score")
plt.ylabel("Description")
plt.title("Visualization of Bedroom Design Preferences")
plt.yticks(y, labels)  # y軸のラベルを設定
plt.legend()  # 凡例を表示
plt.gca().invert_yaxis()  # Y軸を反転させる
plt.show()
