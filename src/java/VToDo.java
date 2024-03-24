/*======================================================================
 FILE: VToDo.java
 CREATOR: fnguyen 01/11/02
 SPDX-FileCopyrightText: 2002, Critical Path
 SPDX-License-Identifier: LGPL-2.1-only OR MPL-2.0
======================================================================*/

package net.cp.jlibical;

public class VToDo extends VComponent {
	public VToDo()
	{
		super(ICalComponentKind.ICAL_VTODO_COMPONENT);
	}

	public VToDo(long obj)
	{
		super(obj);
	}

	public VToDo(String str)
	{
		super(str);
	}
}
