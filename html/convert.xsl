<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
   <xsl:template match="/">
      <html>
         <body>
            <h1>HTML report</h1>
            <table border="1">
               <tr>
	          <th bgcolor="blue">id</th>
		      <th bgcolor="blue">first_name</th>
		      <th bgcolor="blue">last_name</th>
		      <th bgcolor="blue">avatar</th>
			  <th bgcolor="blue">email</th>
               </tr>
               <xsl:for-each select="report/project">
                  <tr>
		          <td>
                        <xsl:value-of select="id" />
                  </td>
		          <td>
                        <xsl:value-of select="first_name" />
                  </td>
                  <td>
                        <xsl:value-of select="last_name" />
                  </td>
				  <td>
                        <xsl:value-of select="avatar" />
                  </td>
				   <td>
                        <xsl:value-of select="email" />
                  </td>
                     </tr>
               </xsl:for-each>
            </table>
         </body>
      </html>
   </xsl:template>
</xsl:stylesheet>
