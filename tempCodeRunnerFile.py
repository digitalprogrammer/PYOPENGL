      bumpMaterial = LambertMaterial(texture=colorTex, bumpTexture=bumpTex, properties={"bumpStrength":1})
        mesh = Mesh(geometry, bumpMaterial)