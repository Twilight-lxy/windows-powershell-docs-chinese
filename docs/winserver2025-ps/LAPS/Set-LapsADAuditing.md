---
description: 配置一个 Active Directory（AD）组织单元（Organizational Unit，简称 OU），以启用对 Windows 本地管理员密码解决方案（Windows Local Administrator Password Solution，简称 LAPS）中的密码模式属性的审计功能。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/set-lapsadauditing?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Set-LapsADAuditing
---

# Set-LapsADAuditing

## 摘要
配置 Active Directory（AD）的组织单位（Organizational Unit，简称 OU），以便对 Windows 本地管理员密码解决方案（Windows Local Administrator Password Solution，简称 LAPS）中的密码模式属性启用审计功能。

## 语法

```
Set-LapsADAuditing [-Credential <PSCredential>] -Identity <String[]> -AuditedPrincipals <String[]>
 [-AuditType <AuditFlags>] [-Domain <String>] [-DomainController <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
{{ 填写描述内容 }}

## 示例

### 示例 1

```powershell
Set-LapsADAuditing -Identity LapsTestOU -AuditedPrincipals "laps.com\LapsAdmin" -AuditType Success
OU=LapsTestOU,DC=laps,DC=com
```

这个示例演示了如何在某个组织单元（OU）上配置“成功”审计规则。

### 示例 2

```powershell
Set-LapsADAuditing -Identity LapsTestOU -AuditedPrincipals "laps.com\LapsAdminsGroup" -AuditType Failure
OU=LapsTestOU,DC=laps,DC=com
```

这个示例演示了如何在某个组织单位（OU）上配置“失败”审计（Failure audits）。

## 参数

### -AuditedPrincipals

指定需要配置审计功能的用户或组的名称。用户或组可以以名称（name）或SID（Security Identifier）的格式进行指定。如果采用名称格式进行指定，名称中必须始终包含用于识别的域名部分，除非该名称对应的是一个众所周知的内置账户。

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

### -AuditType

指定是否配置成功审计或失败审计功能。

```yaml
Type: System.Security.AccessControl.AuditFlags
Parameter Sets: (All)
Aliases:
Accepted values: None, Success, Failure

Required: False
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

指定要更新的组织的名称（OU）。

此参数支持几种不同的名称格式，这些格式会影响最终AD搜索中使用的标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- name (for all other inputs)

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

在运行该cmdlet之前，会提示您进行确认。

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

展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

[Windows LAPS 概述](https://go.microsoft.com/fwlink/?linkid=2233901)
