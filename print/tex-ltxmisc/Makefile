# $NetBSD: Makefile,v 1.9 2019/12/06 20:21:56 markd Exp $

DISTNAME=	ltxmisc
PKGNAME=	tex-${DISTNAME}-2010.21927
TEXLIVE_REV=	21927

MAINTAINER=	minskim@NetBSD.org
COMMENT=	Miscellaneous LaTeX packages

DEPENDS+=	tex-beton-[0-9]*:../../print/tex-beton
DEPENDS+=	tex-latex-bin-[0-9]*:../../print/tex-latex-bin
DEPENDS+=	tex-euler-[0-9]*:../../print/tex-euler
DEPENDS+=	tex-graphics-[0-9]*:../../print/tex-graphics
DEPENDS+=	tex-latex-[0-9]*:../../print/tex-latex
DEPENDS+=	tex-minitoc-[0-9]*:../../print/tex-minitoc
DEPENDS+=	tex-natbib-[0-9]*:../../print/tex-natbib
DEPENDS+=	tex-psnfss-[0-9]*:../../fonts/tex-psnfss
DEPENDS+=	tex-tools-[0-9]*:../../print/tex-tools

TEXLIVE_UNVERSIONED=	yes
.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
