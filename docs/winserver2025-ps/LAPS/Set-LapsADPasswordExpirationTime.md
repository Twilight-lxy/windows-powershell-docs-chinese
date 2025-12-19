---
description: 用于设置 Active Directory（AD）计算机或域控制器对象上的 Windows 本地管理员密码解决方案（LAPS）密码过期时间戳。
external help file: lapspsh.dll-Help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/set-lapsadpasswordexpirationtime?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Set-LapsADPasswordExpirationTime
---

# 设置 LAPsAD 密码过期时间

## 摘要
用于设置 Windows 本地管理员密码解决方案（LAPS）的密码过期时间戳，适用于 Active Directory（AD）计算机或域控制器对象。

## 语法

```
Set-LapsADPasswordExpirationTime [-Credential <PSCredential>] -Identity <String[]>
 [-WhenEffective <DateTime>] [-Domain <String>] [-DomainController <String>] [<CommonParameters>]
```

## 描述

`Set-LapsADPasswordExpirationTime` 这个 cmdlet 被管理员用来配置 AD 电脑或域控制器对象上的密码过期时间。

> [!提示] > 运行此cmdlet会设置AD计算机或域控制器对象上的LAPS密码过期时间，但新的过期时间直到目标设备下次执行LAPS策略处理周期时才会生效。

## 示例

### 示例 1

```powershell
Set-LapsADPasswordExpirationTime -Identity lapsClient
```

```Output
DistinguishedName                           Status
-----------------                           ------
CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com  PasswordReset
```

这个示例展示了将LAPS密码的过期时间设置为当前时间，这样密码就会立即失效。

### 示例 2

```powershell
Set-LapsADPasswordExpirationTime -Identity lapsClient -WhenEffective (Get-Date -Date "07/04/2023 13:00:00")
```

```Output
DistinguishedName                           Status
-----------------                           ------
CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com  PasswordReset
```

这些示例展示了如何将LAPS密码的过期时间设置为某个特定的日期。

### 示例 3

```powershell
Set-LapsADPasswordExpirationTime -Identity lapsClient -WhenEffective ([DateTime]::Now.AddDays(1))
```

```Output
DistinguishedName                           Status
-----------------                           ------
CN=LAPSCLIENT,OU=LapsTestOU,DC=laps,DC=com  PasswordReset
```

这些示例展示了如何将LAPS密码的过期时间设置为未来的一天。

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

指定要设置LAPS密码过期时间的计算机或域控制器对象的名称。

此参数支持多种不同的名称格式，这些格式会影响在 Active Directory（AD）中搜索目标设备时所使用的相关标准。支持的名称格式如下：

- distinguishedName (begins with a `CN=`)
- samAccountName (begins with a `$`)
- dnsHostName (contains at least one `.` character)
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

### -WhenEffective

指定新的LAPS密码过期时间。如果未指定，则使用当前时间，此时密码将立即失效。

```yaml
Type: System.DateTime
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

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)
