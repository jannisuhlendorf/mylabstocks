<?php
session_start ();
require("headers.php");

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
$opts['key'] = 'id';

// Type of key field (int/real/string/date etc.)
$opts['key_type'] = 'int';

// Sorting field(s)
$opts['sort_field'] = array('ID');

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

$opts['fdd']['id'] = array(
  'name'     => 'ID',
  'select'   => 'N',
  //'options'  => 'AVCPDR', // auto increment
  'maxlen'   => 10,
  'default'  => '0',
  'sort'     => true
);

$opts['fdd']['Antigen'] = array(
  'name'     => 'Antigen',
  'select'   => 'T',
  'maxlen'   => 50,
  'sort'     => true
);
$opts['fdd']['InStock'] = array(
  'name'     => 'InStock',
  'select'   => 'D',
  'maxlen'   => 20,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'ab_avail',
	'column' => 'Type')
);
$opts['fdd']['ProductID'] = array(
  'name'     => 'Product-ID',
  'select'   => 'T',
  'maxlen'   => 50,
  'sort'     => true
);
$opts['fdd']['Host'] = array(
  'name'     => 'Host',
  'select'   => 'D',
  'maxlen'   => 50,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'ab_host',
	'column' => 'Host')
);
$opts['fdd']['Type'] = array(
  'name'     => 'Type',
  'select'   => 'D',
  'maxlen'   => 20,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'ab_type',
	'column' => 'Type')
);
$opts['fdd']['Ordered_by'] = array(
  'name'     => 'Ordered_by',
  'select'   => 'D',
  'maxlen'   => 25,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'lab_members',
	'column' => 'id')
);
$opts['fdd']['Date'] = array(
  'name'     => 'Date ',
  'select'   => 'N',
  'maxlen'   => 10,
  'sort'     => true,
  'default'  => date("Y-m-d", strtotime("now"))
);
$opts['fdd']['Dilution-WB'] = array(
  'name'     => 'WB-dilution',
  'select'   => 'T',
  'maxlen'   => 50,
  'sort'     => true
);
$opts['fdd']['Volume-ChIP'] = array(
  'name'     => 'ChIP-volume',
  'select'   => 'T',
  'maxlen'   => 40,
  'sort'     => true
);
$opts['fdd']['Supplier'] = array(
  'name'     => 'Supplier',
  'select'   => 'D',
  'maxlen'   => 20,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'ab_supplier',
	'column' => 'Supplier')
);
$opts['fdd']['Batch_Reference'] = array(
  'name'     => 'BatchRef',
  'select'   => 'T',
  'maxlen'   => 50,
  'sort'     => true
);
$opts['fdd']['Location'] = array(
  'name'     => 'Location',
  'select'   => 'T',
  'maxlen'   => 200,
  'sort'     => true
);
$opts['fdd']['Comments'] = array(
  'name'     => 'Comments',
  'select'   => 'T',
  'maxlen'   => 200,
  'sort'     => true
);
$opts['fdd']['storage_minus20freezers'] = array(
  'name'     => '-20 Freezer',
  'select'   => 'D',
  'maxlen'   => 25,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'storage_minus20freezers',
	  'column' => 'name'),
  'default'  => 'Amp'
);
$opts['fdd']['storage_minus80freezers'] = array(
  'name'     => '-80 Freezer',
  'select'   => 'D',
  'maxlen'   => 25,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'storage_minus80freezers',
	  'column' => 'name'),
  'default'  => 'Amp'
);
$opts['fdd']['storage_fridges'] = array(
  'name'     => 'Fridge',
  'select'   => 'D',
  'maxlen'   => 25,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'storage_fridges',
	  'column' => 'name'),
  'default'  => 'Amp'
);
$opts['fdd']['storage_rooms'] = array(
  'name'     => 'Room',
  'select'   => 'D',
  'maxlen'   => 25,
  'sort'     => true,
  'values'   => array(
  	'table'  => 'storage_rooms',
	  'column' => 'name'),
  'default'  => 'Amp'
);

// TRIGGER
// Before displaying the view page

require("footers.php");
?>