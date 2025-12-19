---
description: 配置 Active Directory（AD）组织单元（OU）的安全设置，以允许特定的用户或组查询 Windows 本地管理员密码解决方案（LAPS）中的密码。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/set-lapsadreadpasswordpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Set-LapsADReadPasswordPermission
---

# 设置 Set-LapsADReadPasswordPermission 的权限

## 摘要
配置 Active Directory（AD）组织单元（OU）的安全设置，以允许特定的用户或组查询 Windows 本地管理员密码解决方案（LAPS）中的密码。

## 语法

```
Set-LapsADReadPasswordPermission [-Credential <PSCredential>] -Identity <String[]>
 -AllowedPrincipals <String[]> [-Domain <String>] [-DomainController <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-LapsADReadPasswordPermission` cmdlet 由管理员使用，用于配置组织单元（OU）的安全权限，以允许特定用户或组查询该 OU 中计算机上的 LAPS 密码。这些用户和组必须使用包含域名和用户名成分的完全限定名称进行标识。唯一的例外情况是，当指定的名称对应于一个内置主体（如 “Domain Admins”）时。

## 示例

### 示例 1

```powershell
Set-LapsADReadPasswordPermission -Identity LapsTestOU -AllowedPrincipals "Domain Admins"
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何使用一个独立的名称来运行该cmdlet，该名称可以成功映射到一个知名的用户或组。

### 示例 2

```powershell
Set-LapsADReadPasswordPermission -Identity LapsTestOU -AllowedPrincipals @("S-1-5-21-2889755270-1324585639-743026605-1215")
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何运行该cmdlet，并将用户的SID作为输入参数进行指定。

### 示例 3

```powershell
Set-LapsADReadPasswordPermission -Identity 'OU=LapsTestOU,DC=laps,DC=com' -AllowedPrincipals @("laps.com\LapsAdmin1", "LapsAdmin2@laps.com")
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何运行 cmdlet，并指定两个采用不同格式的全限定用户名。

### 示例 4

```powershell
Set-LapsADReadPasswordPermission -Identity LapsTestOU -AllowedPrincipals @("LapsAdministratorsGroup")
```

```Output
Set-LapsADReadPasswordPermission : The 'LapsAdministratorsGroup' account appears to be an isolated
name but is not a well-known name. Please use a fully qualified name instead, such as
"LAPSAdmins@contoso.com" or "contoso\LAPSAdmins"
At line:1 char:1
+ Set-LapsADReadPasswordPermission -Identity LapsTestOU -AllowedPrincip ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-LapsADReadPasswordPermission], LapsPowershellException
    + FullyQualifiedErrorId : Invalid principal specified,Microsoft.Windows.LAPS.SetLapsADReadPasswordPermission
```

这个例子展示了一个由于指定了一个无法解析为已知或内置账户的孤立名称而导致的失败。解决这个错误的方法是在输入名称中添加一个域名限定符，例如 `LapsAdministratorsGroup@laps.com`。

## 参数

### -AllowedPrincipals

指定应被授予权限的用户或组的名称。用户或组可以以名称格式或SID格式进行指定。如果以名称格式指定，名称必须始终包含标识域名部分，除非该名称对应于一个众所周知的或内置的账户。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

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

指定要更新的组织单元（OU）的名称。

此参数支持多种不同的名称格式，这些格式会影响最终AD搜索中使用的筛选标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- name (for all other inputs)

在域根上设置权限时，仅支持使用 `distinguishedName` 输入格式，例如 ‘DC=laps,DC=com’。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm

在运行cmdlet之前，会提示您确认是否要继续执行该操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
