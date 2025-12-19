---
description: 配置 Active Directory（AD）组织单元（OU）的安全设置，以允许特定用户或组更改 Windows 本地管理员密码解决方案（LAPS）中的密码过期时间。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/set-lapsadresetpasswordpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Set-LapsADResetPasswordPermission
---

# 设置 Set-LapsADResetPasswordPermission 权限

## 摘要
配置 Active Directory（AD）组织单元（OU）的安全设置，以允许特定用户或组更改 Windows 本地管理员密码解决方案（LAPS）中的密码过期时间。

## 语法

```
Set-LapsADResetPasswordPermission [-Credential <PSCredential>] -Identity <String[]>
 -AllowedPrincipals <String[]> [-Domain <String>] [-DomainController <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-LapsADResetPasswordPermission` cmdlet 由管理员使用，用于配置某个组织单位（OU）的安全权限，以便允许特定用户或组在该 OU 内的计算机上重置 LAPS 密码的有效期。用户名和组名必须包含完整的域名称和用户名两部分。唯一的例外情况是当指定的名称对应于一个内置的主体（如 `Domain Admins`）时。

## 示例

### 示例 1

```powershell
Set-LapsADResetPasswordPermission -Identity LapsTestOU -AllowedPrincipals "Domain Admins"
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何使用一个独立的名字来运行该cmdlet，该名字能够成功映射到一个众所周知的用户或组。

### 示例 2

```powershell
Set-LapsADResetPasswordPermission -Identity LapsTestOU -AllowedPrincipals @("S-1-5-21-2889755270-1324585639-743026605-1215")
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何运行该cmdlet，并将用户SID作为输入参数进行指定。

### 示例 3

```powershell
Set-LapsADResetPasswordPermission -Identity 'OU=LapsTestOU,DC=laps,DC=com' -AllowedPrincipals @("laps.com\LapsAdmin1", "LapsAdmin2@laps.com")
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例展示了如何运行 cmdlet，并指定两个采用不同格式的全限定用户名。

### 示例 4

```powershell
Set-LapsADResetPasswordPermission -Identity LapsTestOU -AllowedPrincipals @("LapsAdministratorsGroup")
```

```Output
Set-LapsADReadPasswordPermission : The 'LapsAdministratorsGroup' account appears to be an isolated
name but is not a well-known name. Please use a fully qualified name instead, such as
"LapsAdministratorsGroup@contoso.com" or "contoso\LapsAdministratorsGroup"
At line:1 char:1
+ Set-LapsADReadPasswordPermission -Identity LapsTestOU -AllowedPrincip ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-LapsADReadPasswordPermission], LapsPowershellException
    + FullyQualifiedErrorId : Invalid principal specified,Microsoft.Windows.LAPS.SetLapsADReadPasswordPermission
```

这个例子展示了一个由于指定了一个无法解析为已知或内置账户的独立名称而导致的失败。解决这个错误的方法是在输入名称中添加一个域名限定符，例如 “LapsAdministratorsGroup@laps.com”。

## 参数

### -AllowedPrincipals

指定应被授予权限的用户或组的名称。用户或组可以以名称格式或SID格式进行指定。如果使用名称格式进行指定，名称中必须始终包含标识域名部分，除非该名称对应于一个众所周知的或内置的账户。

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

指定要更新的OU（组织单位）的名称。

此参数支持多种不同的名称格式，这些格式会影响最终AD搜索中使用的标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- name (for all other inputs)

仅支持使用 `distinguishedName` 输入格式来设置域根的权限，例如 ‘DC=laps,DC=com’。

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

在运行cmdlet之前，会提示您进行确认。

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

展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
