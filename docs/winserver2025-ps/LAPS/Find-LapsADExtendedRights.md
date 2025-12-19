---
description: 查询 Active Directory（AD），以找到那些被授予读取 Windows 本地管理员密码解决方案（LAPS）密码属性权限的主体。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/find-lapsadextendedrights?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Find-LapsADExtendedRights
---

# Find-LapsADExtendedRights

## 摘要
查询 Active Directory（AD），以找到被授予读取 Windows 本地管理员密码解决方案（LAPS）密码属性权限的主体。

## 语法

```
Find-LapsADExtendedRights [-Credential <PSCredential>] -Identity <String[]> [-Domain <String>]
 [-DomainController <String>] [-IncludeComputers] [<CommonParameters>]
```

## 描述

`Find-LapsADExtendedRights` cmdlet 由管理员使用，用于查询哪些主体被授予了读取 LAPS 密码属性的权限。

## 示例

### 示例 1

```powershell
Find-LapsADExtendedRights -Identity LapsTestOU
```

```Output
ObjectDN                     ExtendedRightHolders
--------                     --------------------
OU=LapsTestOU,DC=laps,DC=com {NT AUTHORITY\SYSTEM, LAPS\Domain Admins, LAPS\LapsAdmins}
```

这个例子展示了如何运行该cmdlet。

## 参数

### -Credential

指定在更新 Active Directory (AD) 时使用的凭据。如果未指定，则使用当前用户的凭据。

```yaml
Type: System.Management.Automation.PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Domain

指定要连接的域的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DomainController

指定要连接的域控制器的名称。

```yaml
Type: System.String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identity

指定要查询的组织单位（Organizational Unit, OU）的名称。

此参数支持多种不同的名称格式，这些格式会影响最终AD搜索中使用的标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- name (for all other inputs)

仅支持使用 `distinguishedName` 输入格式来查询域根的权限，例如 ‘DC=laps,DC=com’。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -IncludeComputers

请指定此参数，以便同时检查计算机对象上的权限设置。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS 概述](https://go.microsoft.com/fwlink/?linkid=2233901)
