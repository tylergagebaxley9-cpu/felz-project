<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TEI [
<!ENTITY om "⸆"><!-- omission (blank first hand reading)-->
]>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" >

<xsl:template match="/">
	<html>
	 	<head>
		 	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		 	<title>Codex Bezae Transcriptions</title>
		 	<script type="text/javascript">
				function gotoTranscriptionPap(mySel)
				{
					var form = document.forms.transnavPap;
					var wit = form.ms[form.ms.selectedIndex].value
					window.parent.location.href = ""+ wit ;
					return false;
				}
			</script>	
<!-- Change the link below for the Uncial version -->
		 	<link rel="stylesheet" href="bezae.css" type="text/css"/>
			<!-- css margin order: top right bottom left --> 
		</head>
	 	<body>
	 		<div id="header">
	 			<a href="http://www.igntp.org/" target="_self">
	 				<span id="logo"><strong>Codex Bezae</strong></span>
	 			</a>
	 			<span id="top"><strong>TRANSCRIPTION</strong></span>
	 		</div>
	 		<div id="navigation">
	 			<p class="menu">
	 				<table>
	 					<tr>
	 						<td>
	 							<i>Complete text:</i>
	 							<br/>
	 							<a href="Bezae-Latin.xml">Latin</a>
	 							<xsl:text>      </xsl:text>
	 							<a href="Bezae-Greek.xml">Greek </a>
	 							<xsl:text>      </xsl:text>
	 							<a href="Bezae-Uncial.xml">Greek uncial</a>
	 							<xsl:text>      </xsl:text>
	 							<a href="Greek-Latin.htm">Both columns</a>
	 						</td>
	 						<td><xsl:text>        </xsl:text></td>
	 						<td>
	 							<i>Select by book:</i>
	 							<form action="" name="transnavPap" id="transnavpap">
		 							<select name="ms" onChange="gotoTranscriptionPap();">
		 								<option value="">Select Book</option>
		 								<option value="01_MtGk.xml">Matthew (Greek)</option>
		  								<option value="01_MtLat.xml">Matthew (Latin)</option>
										<option value="04_JnGk.xml">John (Greek)</option>
		 								<option value="04_JnLat.xml">John (Latin)</option>
		  								<option value="03_LcGk.xml">Luke (Greek)</option>
		 								<option value="03_LcLat.xml">Luke (Latin)</option>
		  								<option value="02_McGk.xml">Mark (Greek)</option>
		   								<option value="02_McLat.xml">Mark (Latin)</option>
		 								<option value="25_3JnLat.xml">3 John (Latin)</option>
		 								<option value="05_AcGk.xml">Acts (Greek)</option>
		 								<option value="05_AcLat.xml">Acts (Latin)</option>
		 								<option value="06_2colpages.xml">Two column pages</option>
		 							</select>
	 							</form>
	 						</td>
	 						<td><xsl:text>     </xsl:text></td>
	 						<td>
	 							<i>Further information:</i>
	 							<br/>
	 							<a href="Bezae-key.xml">Key to the transcription</a>
	 						</td>
	 					</tr>			
	 				</table>
<!-- add the link to the font here for the uncial setting -->
				</p> 
			</div> <!-- end navigation -->
	
			<p>
				<h2>
					<xsl:for-each select="tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt">
						<xsl:value-of select="tei:title"/>
	 				</xsl:for-each>
	 			</h2>
				<span class="title">
					<strong>
						<xsl:for-each select="tei:TEI/tei:teiHeader/tei:fileDesc/tei:sourceDesc/tei:msDesc/tei:msIdentifier">
	 						<xsl:value-of select="tei:msName"/>
	 						<xsl:text>: </xsl:text>
	 						<xsl:value-of select="tei:settlement"/>
	 						<xsl:text>, </xsl:text>
	 						<xsl:value-of select="tei:repository"/>
	 						<xsl:text>: </xsl:text>
	 						<xsl:value-of select="tei:idno"/>
	 					</xsl:for-each>
	 				</strong>
	 				<br/>
	 			</span>
	 		</p>
			<div id="hyperlinks-top">
				<!--xsl:for-each select="tei:TEI/tei:teiHeader/tei:encodingDesc/tei:projectDesc">
				<xsl:choose>
				<xsl:when test="@n='key'"></xsl:when>
				<xsl:otherwise-->
				<p>
					<xsl:text>Folios: </xsl:text>
					<select id="page_select" onchange="javascript:window.location='#' + this.value">
						<option value="">Select Folio</option>
						<xsl:for-each select="tei:TEI//tei:pb">
							<option>							
								<xsl:attribute name="value">
									<xsl:value-of select="@n"/>
								</xsl:attribute>
								<xsl:value-of select="@n"/>
							</option>
						</xsl:for-each>
					</select>
					<xsl:text> Books: </xsl:text> 		
					<select id="page_select" onchange="javascript:window.location='#' + this.value">
						<option value="">Select Book</option>
						<xsl:for-each select="tei:TEI//tei:div[@type='book']">
							<option>
								<xsl:attribute name="value">
									<xsl:value-of select="@n"/>
								</xsl:attribute>
								<xsl:value-of select="@n"/>
							</option>
						</xsl:for-each>
					</select>
					<xsl:text> Chapters: </xsl:text>
					<select id="chapter_select" onchange="javascript:window.location='#' + this.value">
						<option value="">Select Chapter</option>
						<xsl:for-each select="tei:TEI//tei:div[@type='chapter']">
							<option>
								<xsl:attribute name="value">
									<xsl:value-of select="@n"/>
								</xsl:attribute>
								<xsl:value-of select="concat(./ancestor::tei:div[@type='book']/@n, ' ', substring-after(@n,'K'))"/>
							</option>
						</xsl:for-each>
					</select>
				</p>
				<!--/xsl:otherwise>
				</xsl:choose>
				</xsl:for-each-->
			</div>
			<div id="text">
	 			<xsl:apply-templates/> 
				<hr/>
			</div>
		</body>
	</html>
</xsl:template>


<!-- Text stuff -->
<xsl:template match="text()" mode="title">
	<xsl:value-of select="."/>
	<xsl:text> </xsl:text>
</xsl:template>

<xsl:template match="text()" mode="title-nospace">
	<xsl:value-of select="."/>
</xsl:template>


<!-- Page layout-->
<xsl:template match="tei:pb">
	<hr id="{@n}" />
	<span class="pageheader">
		<p>
			<xsl:text>Folio </xsl:text>
			<xsl:value-of select="@n"/>
			<xsl:text>   </xsl:text>
			<a>
				<xsl:attribute name="href">
					<xsl:value-of select="@facs"/>
				</xsl:attribute>
				<xsl:text>Image</xsl:text>
			</a>
			<xsl:text>   </xsl:text>
			<xsl:value-of select="@type"/>
			<xsl:text> (</xsl:text>
			<xsl:value-of select="@subtype"/>
			<xsl:text>)      </xsl:text>
			<span class="italic">
				<xsl:value-of select="(./ancestor::tei:div[@type='book']/@n)"/> 
				<xsl:value-of select="substring-after(./ancestor::tei:div[@type='chapter']/@n, 'K')"/>
			</span>
            <a href="#top">
				<i>back to top</i>
			</a>
		</p>
	</span>
</xsl:template>

<xsl:template match="tei:lb">
	<br/>
	<span class="line_number" title="Line number">
		<xsl:choose>
			<xsl:when test="@n='3'"><xsl:value-of select="@n"/><xsl:text> </xsl:text></xsl:when>
			<xsl:when test="@n='6'"><xsl:value-of select="@n"/><xsl:text> </xsl:text></xsl:when>
			<xsl:when test="@n='9'"><xsl:value-of select="@n"/><xsl:text> </xsl:text></xsl:when>
			<xsl:when test="@n='12'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='15'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='18'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='21'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='24'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='27'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='30'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='33'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:when test="@n='36'"><xsl:value-of select="@n"/></xsl:when>
			<xsl:otherwise><xsl:text>    </xsl:text></xsl:otherwise>
		</xsl:choose>
	</span>
	<xsl:choose>
		<xsl:when test="@rend">
			<span>
				<xsl:attribute name="class">
					<xsl:value-of select="@rend"/>
				</xsl:attribute>
			</span>
		</xsl:when>
		<xsl:otherwise>
			<span class="line"></span>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<!-- Divisions-->
<xsl:template match="tei:div[@type='book']">
	<span id="{@n}"/>
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="tei:div[@type='chapter']">
	<span class="chapter_number" id="{@n}" title="Modern chapter number">
		<xsl:value-of select="substring-after(@n,'K')"/>
		<xsl:text>:</xsl:text>
	</span> 
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="tei:ab">
	<span class="verse_number" title="Modern verse number">
		<xsl:value-of select="substring-after(@n,'V')"/>
	</span> 
	<xsl:choose>
		<xsl:when test="@type='supplement'">
			<span class="supplement">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
		<xsl:otherwise>
			<xsl:apply-templates/>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>

<xsl:template match="tei:w">
	<xsl:apply-templates/>
	<xsl:text> </xsl:text>
</xsl:template>

<xsl:template match="tei:pc">
	<xsl:apply-templates/>
	<xsl:text> </xsl:text>
</xsl:template>

<xsl:template match="tei:ex">
	<span class="abbreviation" title="Expansion of abbreviated text">
		<xsl:text>(</xsl:text>
		<xsl:apply-templates/>
		<xsl:text>)</xsl:text>
	</span>
</xsl:template>

<xsl:template match="tei:abbr">
	<xsl:choose>
		<xsl:when test="@type='nomSac'">
			<span title="Nomen sacrum (abbreviation)">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
		<xsl:when test="@type='num'">
			<span title="Numeral (abbreviation)">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
	</xsl:choose>
</xsl:template>

<xsl:template match="tei:div[@type='incipit']">
	<span class="verse_number"><strong>Incipit</strong></span> 
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="tei:div[@type='explicit']">
	<span class="verse_number"><strong>Explicit</strong></span> 
	<xsl:apply-templates/>
</xsl:template>


<!-- Margins-->
<xsl:template match="tei:seg">
	<xsl:choose>
		<xsl:when test="@subtype='lineleft'">
			<span class="marginlineleft">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
		<xsl:when test="@subtype='lineright'">
			<span class="marginlineright">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
		<xsl:when test="@subtype='pagetop'">
			<span class="marginpage">
				<xsl:apply-templates/>
				<br/>
			</span>
		</xsl:when>
		<xsl:when test="@subtype='pagebottom'">
			<br/>
			<br/>
			<span class="marginpage">
				<xsl:apply-templates/>
			</span>
		</xsl:when>
		<xsl:when test="@type='secondColumn'">
			<span class="column2">
				<xsl:choose>
					<xsl:when test="@subtype='center'">
					<xsl:text>                     </xsl:text>
					</xsl:when>
					<xsl:when test="@subtype='hang'">
					<xsl:text></xsl:text>
					</xsl:when>
					<xsl:otherwise>    </xsl:otherwise>
				</xsl:choose>
				<xsl:apply-templates/>
			</span>
		</xsl:when>
	</xsl:choose>
</xsl:template>

<!-- Notes and numbers-->
<xsl:template match="tei:note[@type='editorial']">
	<span>
		<xsl:attribute name="class">
			<xsl:choose>
				<xsl:when test="@place='right'">rightJust</xsl:when>
				<xsl:when test="@place='center'">centerJust</xsl:when>
				<xsl:when test="@place='left'">line</xsl:when>
			</xsl:choose>
		</xsl:attribute>
		<span class="editorialnote">
			<xsl:attribute name="title">
				<xsl:apply-templates mode="title"/>
			</xsl:attribute>
			<xsl:text>Note </xsl:text>
		</span>
	</span>
</xsl:template>

<xsl:template match="tei:note[@type='hermeneia']">
	<span title="Hermeneia">
		<xsl:attribute name="class">
			<xsl:choose>
				<xsl:when test="@place='center'">centerJustmargin</xsl:when>
			</xsl:choose>
		</xsl:attribute>
		<span class="hermeneia">
			<xsl:apply-templates/>
		</span>
	</span>
	<br/>
</xsl:template>

<xsl:template match="tei:note[@type='library']">
	<span>
		<xsl:attribute name="class">
			<xsl:choose>
				<xsl:when test="@place='right'">rightJust</xsl:when>
				<xsl:when test="@place='center'">centerJust</xsl:when>
				<xsl:when test="@place='left'">line</xsl:when>
			</xsl:choose>
		</xsl:attribute>
		<span class="editorialnote">
			<xsl:attribute name="title">
				<xsl:text>Library Note (</xsl:text>
				<xsl:value-of select="@rend"/>
				<xsl:text>): </xsl:text>
				<xsl:apply-templates mode="title-nospace" />
			</xsl:attribute>
			<xsl:text>Library Note </xsl:text>
		</span>
	</span>
</xsl:template>

<xsl:template match="tei:note[@type='titlos']">
	<span>
		<xsl:attribute name="title">
			<xsl:text>Titlos: </xsl:text>
			<xsl:apply-templates/>
		</xsl:attribute>
		<xsl:apply-templates/>
	</span>
	<br/>
</xsl:template>

<xsl:template match="tei:note[@type='jotting']">
	<span>
		<xsl:attribute name="title">
			<xsl:text>Jotting added by later hand: </xsl:text>
			<xsl:apply-templates/>
		</xsl:attribute>
		<xsl:apply-templates/>
	</span>
	<br/>
</xsl:template>

<xsl:template match="tei:num">
<!-- num can be chapNum AmmSec -->
	<span>
		<xsl:attribute name="class">
			<xsl:choose>
				<xsl:when test="@rend='pencil'">pencil</xsl:when>
				<xsl:when test="@rend='ink'">ink</xsl:when>
			</xsl:choose>
		</xsl:attribute>
		<span>
			<xsl:attribute name="title">
				<xsl:choose>
					<xsl:when test="@type='chapNum'">
						<xsl:text>Chapter Number (</xsl:text>
						<xsl:value-of select="@rend"/>
						<xsl:text>): </xsl:text>
						<xsl:apply-templates mode="title-nospace" />
					</xsl:when>
					<xsl:when test="@type='AmmSec'">
						<xsl:text>Ammonian Section </xsl:text>
						<xsl:value-of select="@n"/>
					</xsl:when>
				</xsl:choose>
			</xsl:attribute>
			<xsl:apply-templates/>
		</span>
	</span>
</xsl:template>

<!-- Gap, space, unclear-->
<xsl:template match="tei:gap[not(ancestor::tei:rdg)]">
	<xsl:if test="@reason='lacuna'">
		<span class="supplied" title="Lacuna of {@extent} {@unit}">[...]</span>
	</xsl:if>
	<xsl:if test="@reason='illegible'">
		<span class="supplied" title="{@extent} {@unit} illegible">[...]</span>
	</xsl:if>
</xsl:template>

<xsl:template match="tei:gap[ancestor::tei:rdg]">
	<xsl:text>[...] </xsl:text>
</xsl:template>

<xsl:template match="tei:space">
	<xsl:choose>
		<xsl:when test="@unit='char' and @extent='1'"><xsl:text>  </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='2'"><xsl:text>    </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='3'"><xsl:text>      </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='4'"><xsl:text>        </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='5'"><xsl:text>          </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='6'"><xsl:text>            </xsl:text></xsl:when>
		<xsl:when test="@unit='char' and @extent='7'"><xsl:text>              </xsl:text></xsl:when>
		<xsl:when test="@unit='line'"><br/></xsl:when>
	</xsl:choose>
</xsl:template>

<xsl:template match="tei:unclear">
	<span class="unclear" title="Unclear text"><xsl:apply-templates/></span>
</xsl:template>

<!-- Corrections-->
<xsl:template match="tei:app">
	<span class="original">
		<xsl:attribute name="title">
			<xsl:for-each select="tei:rdg">
				<xsl:choose>
					<xsl:when test="@type='orig'">
						<xsl:text>Original </xsl:text>
							<xsl:text>(</xsl:text>
								<xsl:value-of select="@hand"/>
							<xsl:text>)</xsl:text>
						<xsl:choose>
							<xsl:when test="tei:w/text()='&om;'">
								<xsl:text> omits</xsl:text>
							</xsl:when>
							<xsl:otherwise>
								<xsl:text>: </xsl:text>
								<xsl:apply-templates mode="title" />
							</xsl:otherwise>
						</xsl:choose>				
					</xsl:when>
					<xsl:when test="@type='corr'">
						<xsl:text>;&#13;Corrector </xsl:text>
						<xsl:choose>
							<xsl:when test="@hand='K'"><xsl:text>(s.m.)</xsl:text></xsl:when>
							<xsl:otherwise>
								<xsl:text>(</xsl:text>
								<xsl:value-of select="@hand"/>
								<xsl:text>)</xsl:text>
							</xsl:otherwise>
						</xsl:choose>
						<xsl:choose>
							<xsl:when test="tei:w/text()='&om;'"> deletes</xsl:when>
							<xsl:otherwise><xsl:text>: </xsl:text>
								<xsl:apply-templates mode="title" />
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>
				</xsl:choose>								
			</xsl:for-each>
		</xsl:attribute>
		<xsl:apply-templates/>
	</span>
</xsl:template>

<xsl:template match="tei:rdg">		
	<xsl:choose>
		<xsl:when test="@type='orig'"><span class="original"><xsl:apply-templates/></span></xsl:when>
		<xsl:otherwise></xsl:otherwise>
	</xsl:choose>
</xsl:template>


<!-- Decorations and fw-->
<xsl:template match="tei:hi[@rend='ol']">
	<span style="text-decoration:overline"><xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="tei:hi[@rend='rubric']">
	<span class="rubric" title="Rubricated text"><xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="tei:hi[@rend='bold']">
	<span style="font-weight:bold"><xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="tei:hi[@rend='bolditalic']">
	<span style="font-weight:bold; font-style:italic"><xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="tei:hi[@rend='hyperlink']">
	<a><xsl:attribute name="href"><xsl:text>http://</xsl:text><xsl:apply-templates/></xsl:attribute><xsl:apply-templates/></a>
</xsl:template>

<xsl:template match="tei:hi[@rend='hypermail']">
	<a><xsl:attribute name="href">mailto:<xsl:apply-templates/></xsl:attribute><xsl:apply-templates/></a>
</xsl:template>

<xsl:template match="tei:fw">
<!-- fw can be pageNum quireSig runTitle chapTitle chapRef lectTitle -->
	<span>
		<xsl:attribute name="class">
			<xsl:choose>
				<xsl:when test="@place='right'">rightJust</xsl:when>
				<xsl:when test="@type='runTitle'">runTitle</xsl:when>
				<xsl:when test="@place='center'">centerJustmargin</xsl:when>
				<xsl:when test="@place='left'">line</xsl:when>
			</xsl:choose>
		</xsl:attribute>
		<span>
			<xsl:attribute name="class">
				<xsl:choose>
					<xsl:when test="@rend='pencil'">pencil</xsl:when>
					<xsl:when test="@rend='ink'">ink</xsl:when>
				</xsl:choose>
			</xsl:attribute>
			<span>
				<xsl:attribute name="title">
					<xsl:choose>
						<xsl:when test="@type='pageNum'">Folio Number (<xsl:value-of select="@rend"/>): <xsl:apply-templates mode="title-nospace" /></xsl:when>
						<xsl:when test="@type='quireSig'">Quire Signature (<xsl:value-of select="@rend"/>): <xsl:apply-templates mode="title-nospace" /></xsl:when>
						<xsl:when test="@type='runTitle'">Running Title</xsl:when>
						<xsl:when test="@type='chapRef'">Chapter Reference: <xsl:apply-templates mode="title-nospace" /></xsl:when>
						<xsl:when test="@type='titlos'">Titlos (hand <xsl:value-of select="@rend"/>): <xsl:apply-templates mode="title-nospace" /></xsl:when>
						<xsl:when test="@type='lectTitle'">Lectionary indication (hand <xsl:value-of select="@rend"/>): <xsl:apply-templates mode="title-nospace" /></xsl:when>
					</xsl:choose>
				</xsl:attribute>
				<xsl:choose>
					<xsl:when test="@type='lectTitle'"><span class="lect">Lect.</span></xsl:when>
					<xsl:otherwise><xsl:apply-templates/></xsl:otherwise>
				</xsl:choose>
			</span>
		</span>
	</span>   
</xsl:template>

<!-- Supplied-->
<xsl:template match="tei:supplied">
	<span class="supplied" title="Supplied text (no longer extant or legible)">[<xsl:apply-templates/>]</span>
</xsl:template>

<!-- Old Supplied procedure, which makes Matthew in Latin very slow-->
<!--xsl:template match="tei:supplied">
	<span class="supplied">
	<xsl:if test="
		   not((preceding::text()[ancestor::tei:w])[last()][ancestor::tei:supplied[not(@source='EditioPrinceps')]])
		or not(string(number(translate(child::text(), '- ', '')))='NaN')
		or not(string(number(translate(string(preceding::tei:w[1]//child::text()), '- ', '')))='NaN')
		or not(preceding::tei:w[1]/tei:supplied)
		or name((preceding::tei:gap|preceding::tei:w)[last()]) = 'gap'
		or (not(ancestor::tei:fw) and preceding::tei:w[1]/ancestor::tei:fw)
		or (not(ancestor::tei:rdg) and preceding::tei:w[1]/ancestor::tei:rdg)
		or (ancestor::tei:rdg and not(ancestor::tei:rdg = preceding::tei:w[1]/ancestor::tei:rdg))
	" >[</xsl:if>
	<xsl:apply-templates/>
	<xsl:choose>
		<xsl:when test="
		   not(following::text()[ancestor::tei:w][1][ancestor::tei:supplied[not(@source='EditioPrinceps')]])
		or not(string(number(translate(child::text(), '- ', '')))='NaN')
		or not(string(number(translate(string(following::tei:w[1]//child::text()), '- ', '')))='NaN')
		or not(following::tei:w[1]/tei:supplied)
		or name((following::tei:gap|following::tei:w)[1]) = 'gap'
		or (ancestor::tei:fw and not(following::tei:w[1]/ancestor::fw))
		or (not(ancestor::tei:rdg) and following::tei:w[1]/ancestor::tei:rdg)
		or (ancestor::tei:rdg and not(ancestor::tei:rdg = following::tei:w[1]/ancestor::tei:rdg))
	" >]</xsl:when>
	<xsl:otherwise> </xsl:otherwise>
	</xsl:choose>
	</span>
</xsl:template-->


<!-- header stuff -->
<xsl:template match="tei:titleStmt">
</xsl:template>
<xsl:template match="tei:editionStmt">
</xsl:template>
<xsl:template match="tei:publicationStmt">
</xsl:template>
<xsl:template match="tei:country">
</xsl:template>
<xsl:template match="tei:msName">
</xsl:template>
<xsl:template match="tei:altIdentifier">
</xsl:template>
<xsl:template match="tei:encodingDesc">
</xsl:template>
<xsl:template match="tei:revisionDesc">
</xsl:template>
<xsl:template match="tei:sourceDesc">
</xsl:template>

</xsl:stylesheet>
