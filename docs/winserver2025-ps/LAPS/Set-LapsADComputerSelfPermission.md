---
description: 配置 Active Directory（AD）组织单位（Organizational Unit，简称 OU）的权限，以便该 OU 中的计算机能够更新其 Windows 本地管理员密码解决方案（Local Administrator Password Solution，简称 LAPS）中的密码。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/set-lapsadcomputerselfpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Set-LapsADComputerSelfPermission
---

# 设置 Set-LapsADComputerSelfPermission 的值

## 摘要
配置 Active Directory（AD）组织单位（OU）的权限，以允许该 OU 中的计算机更新其 Windows 本地管理员密码解决方案（LAPS）的密码。

## 语法

```
Set-LapsADComputerSelfPermission -Identity <String[]> [-Domain <String>]
 [-DomainController <String>] [-Credential <PSCredential>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述

`Set-LapsADComputerperms` 这个 cmdlet 被管理员用来配置某个组织单元（OU）的安全权限，以允许该 OU 中的计算机更新它们的 LAPS 密码。

## 示例

#### 示例 1

```powershell
Set-LapsADComputerSelfPermission -Identity LapsTestOU
```

```Output
Name       DistinguishedName
----       -----------------
LapsTestOU OU=LapsTestOU,DC=laps,DC=com
```

这个示例演示了如何运行该cmdlet。

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

指定要更新的OU（组织单位）的名称。

此参数支持几种不同的名称格式，这些格式会影响最终AD搜索中使用的标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- name (for all other inputs)

在域根设置权限时，仅支持使用 `distinguishedName` 输入格式，例如 ‘DC=laps,DC=com’。

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

### -Confirm

在运行 cmdlet 之前会提示您进行确认。

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

展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
