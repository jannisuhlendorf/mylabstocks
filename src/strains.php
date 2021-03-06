<?php
session_start ();
require("headers.php");



if ($session->mode == "super") {
  print("<p><a href='publish_it.php'>Publish genotypes.</a></p>");
}


// if (array_key_exists("action", $_REQUEST)) {
//   if ($_REQUEST["action"] == "SEARCH_IN_GENOTYPE") {
//     $keys = split(" ", $_REQUEST["geno"]); 
//     print_r($keys );
// 
//     $tmp_filter = "ynl095c:PBY-306-ynl095C";
//     $likes = "";
//     foreach ($keys as $k) {
//       if ($k != "") {
//         $likes .= "`locus1` LIKE '%$k%' OR `locus2` LIKE '%$k%' OR `locus3` LIKE '%$k%' OR `locus4` LIKE '%$k%' OR `locus5` LIKE '%$k%' OR `ADE2` LIKE '%$k%' OR `HIS3` LIKE '%$k%' OR `LEU2` LIKE '%$k%' OR `LYS2` LIKE '%$k%' OR `MET15` LIKE '%$k%' OR `TRP1` LIKE '%$k%' OR `URA3` LIKE '%$k%' OR `HO_` LIKE '%$k%' OR `Cytoplasmic_Character` LIKE '%$k%' ";
//       }
//     }
//     $opts["filters"] = $likes . " " ;
//   }
// }
// 
// if (!array_key_exists("PME_sys_operation", $_REQUEST)) {
//   if (array_key_exists("geno", $_REQUEST)) {
//     $geno = $_REQUEST["geno"]; 
//   } else {
//     $geno = "";
//   }
//   echo "<form action='' method='post'>";
//   //echo "<fieldset style='border:1px plain black; width: 300px;'>";
//   //echo "<legend>Search in genotype</legend>";
//   echo "Search in genotype: <input type='hidden' name='action' value='SEARCH_IN_GENOTYPE'/>";
//   echo "<input type='text' name='geno' value='$geno'/>";
//   echo "<input type='button' name='send' value='Search' onclick='return this.form.submit();'/>";
// //  echo "</fieldset>";
//   echo "</form>";
// }

/*
 * IMPORTANT NOTE: This generated file contains only a subset of huge amount
 * of options that can be used with phpMyEdit. To get information about all
 * features offered by phpMyEdit, check official documentation. It is available
 * online and also for download on phpMyEdit project management page:
 *
 * http://platon.sk/projects/main_page.php?project_id=5
 *
 * This file was generated by:
 *
 *                    phpMyEdit version: unknown
 *       phpMyEdit.class.php core class: 1.204
 *            phpMyEditSetup.php script: 1.50
 *              generating setup script: 1.50
 */


/*************************/
//
// Pass phpMyEdit options
//
/*************************/

$opts['dbh'] = $connexion;
$opts['tb'] = $tb;

// Name of field which is the unique key
$opts['key'] = 'EKY';

// Type of key field (int/real/string/date etc.)
$opts['key_type'] = 'int';

// Sorting field(s)
$opts['sort_field'] = array('EKY');

// Number of records to display on the screen
// Value of -1 lists all records in a table
$opts['inc'] = 15;

// Options you wish to give the users
// A - add,  C - change, P - copy, V - view, D - delete,
// F - filter, I - initial sort suppressed
$opts['options'] = $privopt;

// Number of lines to display on multiple selection filters
$opts['multiple'] = '4';

// Navigation style: B - buttons (default), T - text links, G - graphic links
// Buttons position: U - up, D - down (default)
$opts['navigation'] = 'UDBG';

// Display special page elements
$opts['display'] = array(
	'form'  => true,
	'query' => true,
	'sort'  => true,
	'time'  => true,
	'tabs'  => true
);

// Set default prefixes for variables
$opts['js']['prefix']               = 'PME_js_';
$opts['dhtml']['prefix']            = 'PME_dhtml_';
$opts['cgi']['prefix']['operation'] = 'PME_op_';
$opts['cgi']['prefix']['sys']       = 'PME_sys_';
$opts['cgi']['prefix']['data']      = 'PME_data_';

/* Get the user's default language and use it if possible or you can
   specify particular one you want to use. Refer to official documentation
   for list of available languages. */
$opts['language'] = $_SERVER['HTTP_ACCEPT_LANGUAGE'] . '-UTF8';

/* Table-level filter capability. If set, it is included in the WHERE clause
   of any generated SELECT statement in SQL query. This gives you ability to
   work only with subset of data from table.

$opts['filters'] = "column1 like '%11%' AND column2<17";
$opts['filters'] = "section_id = 9";
$opts['filters'] = "PMEtable0.sessions_count > 200";
*/

/* Field definitions
   
Fields will be displayed left to right on the screen in the order in which they
appear in generated list. Here are some most used field options documented.

['name'] is the title used for column headings, etc.;
['maxlen'] maximum length to display add/edit/search input boxes
['trimlen'] maximum length of string content to display in row listing
['width'] is an optional display width specification for the column
          e.g.  ['width'] = '100px';
['mask'] a string that is used by sprintf() to format field output
['sort'] true or false; means the users may sort the display on this column
['strip_tags'] true or false; whether to strip tags from content
['nowrap'] true or false; whether this field should get a NOWRAP
['select'] T - text, N - numeric, D - drop-down, M - multiple selection
['options'] optional parameter to control whether a field is displayed
  L - list, F - filter, A - add, C - change, P - copy, D - delete, V - view
            Another flags are:
            R - indicates that a field is read only
            W - indicates that a field is a password field
            H - indicates that a field is to be hidden and marked as hidden
['URL'] is used to make a field 'clickable' in the display
        e.g.: 'mailto:$value', 'http://$value' or '$page?stuff';
['URLtarget']  HTML target link specification (for example: _blank)
['textarea']['rows'] and/or ['textarea']['cols']
  specifies a textarea is to be used to give multi-line input
  e.g. ['textarea']['rows'] = 5; ['textarea']['cols'] = 10
['values'] restricts user input to the specified constants,
           e.g. ['values'] = array('A','B','C') or ['values'] = range(1,99)
['values']['table'] and ['values']['column'] restricts user input
  to the values found in the specified column of another table
['values']['description'] = 'desc_column'
  The optional ['values']['description'] field allows the value(s) displayed
  to the user to be different to those in the ['values']['column'] field.
  This is useful for giving more meaning to column values. Multiple
  descriptions fields are also possible. Check documentation for this.
*/

$opts['fdd']['EKY'] = array(
  'name'     => 'EKY',
  'select'   => 'T',
  'maxlen'   => 10,
  'sort'     => true
);
$opts['fdd']['Name_'] = array(
  'name'     => 'Name ',
  'select'   => 'T',
  'maxlen'   => 750,
  'sort'     => true
);
$opts['fdd']['Date_'] = array(
  'name'     => 'Date ',
  'select'   => 'T',
  'maxlen'   => 10,
  'sort'     => true
);
$opts['fdd']['Genotype'] = array(
  'name'     => 'Genotype',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['Phenotype'] = array(
  'name'     => 'Phenotype',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['Growth_req'] = array(
  'name'     => 'Growth req',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['original_no'] = array(
  'name'     => 'Original no',
  'select'   => 'T',
  'maxlen'   => 10,
  'sort'     => true
);
$opts['fdd']['Comments'] = array(
  'name'     => 'Comments',
  'select'   => 'T',
  'maxlen'   => 4294967295,
  'textarea' => array(
    'rows' => 5,
    'cols' => 50),
  'sort'     => true
);
$opts['fdd']['General_Background'] = array(
  'name'     => 'General Background',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['Mating_Type'] = array(
  'name'     => 'Mating Type',
  'select'   => 'T',
  'maxlen'   => 150,
  'sort'     => true
);
$opts['fdd']['Plasmid'] = array(
  'name'     => 'Plasmid',
  'select'   => 'T',
  'maxlen'   => 10,
  'values' => array(
    'table'  => 'plasmids',
    'column' => 'EKP',
    'description' => array(
      'columns' => array( 'Name_plasmid', 'EKP' ),
      'divs' => array( ' (', ')' )
      )),
  'sort'     => true
);
$opts['fdd']['virt'] = array(
  'name'     => 'Plasmid link',
  'select'   => 'T',
  'input'    => 'V',
  'maxlen'   => 300,
  'sort'     => true,
  'sql'      => 'Plasmid',
  'URL'      => 'plasmids.php?PME_sys_fl=0&PME_sys_fm=0&PME_sys_operation=PME_op_View&PME_sys_rec=$value'
);
$opts['fdd']['ADE2'] = array(
  'name'     => 'ADE2',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['HIS3'] = array(
  'name'     => 'HIS3',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['LEU2'] = array(
  'name'     => 'LEU2',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['LYS2'] = array(
  'name'     => 'LYS2',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['TRP1'] = array(
  'name'     => 'TRP1',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['URA3'] = array(
  'name'     => 'URA3',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['HO_'] = array(
  'name'     => 'HO ',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['MET15'] = array(
  'name'     => 'MET15',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['locus1'] = array(
  'name'     => 'Locus1',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['locus2'] = array(
  'name'     => 'Locus2',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['locus3'] = array(
  'name'     => 'Locus3',
  'select'   => 'T',
  'maxlen'   => 300,
  'sort'     => true
);
$opts['fdd']['Parental_strain'] = array(
  'name'     => 'Parental strain',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['Obtained_by'] = array(
  'name'     => 'Obtained by',
  'select'   => 'T',
  'maxlen'   => 750,
  'sort'     => true
);
$opts['fdd']['Reference_'] = array(
  'name'     => 'Reference ',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['clone_no'] = array(
  'name'     => 'Clone no',
  'select'   => 'T',
  'maxlen'   => 10,
  'sort'     => true
);
$opts['fdd']['SGD_ID'] = array(
  'name'     => 'SGD ID',
  'select'   => 'T',
  'maxlen'   => 45,
  'sort'     => true,
  'URL'      => 'http://yeastgenome.org/locus/$value/overview',
  'URLtarget'=> '_blank'
);
$opts['fdd']['labbook_reference'] = array(
  'name'     => 'Labbook reference',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);
$opts['fdd']['Cytoplasmic_Character'] = array(
  'name'     => 'Cytoplasmic Character',
  'select'   => 'T',
  'maxlen'   => 750,
  'sort'     => true
);
$opts['fdd']['Author'] = array(
  'name'     => 'Author',
  'select'   => 'T',
  'maxlen'   => 150,
  'values' => array(
    'table'  => 'lab_members',
    'column' => 'id'
  ),

  'sort'     => true
);
$opts['fdd']['storage_box'] = array(
  'name'     => 'Storage box',
  'select'   => 'T',
  'maxlen'   => 1500,
  'sort'     => true
);


// TRIGGER
// Before displaying the view page
$opts['triggers']['select']['pre'][] = 'strains.TSP.php';
$opts['triggers']['select']['pre'][]    = 'strains.MVC.php';
$opts['triggers']['update']['pre'][]    = 'strains.MVC.php';


require("footers.php");
?>
