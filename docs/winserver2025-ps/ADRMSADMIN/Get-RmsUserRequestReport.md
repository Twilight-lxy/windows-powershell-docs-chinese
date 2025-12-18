---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmsuserrequestreport?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsUserRequestReport
---

# Get-RmsUserRequestReport

## 摘要
生成用于AD RMS集群的用户请求统计报告。

## 语法

```
Get-RmsUserRequestReport [-StartTime <DateTime>] [-EndTime <DateTime>] [-UserName <String>]
 [-RequestType <String>] [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsUserRequestReport` cmdlet 生成一份报告，其中包含有关 Active Directory 权限管理服务（AD RMS）集群中单个用户请求活动的统计数据。

要获取报告，请指定需要生成报告的用户的*用户名*，然后将*路径*参数设置为 AD RMS 提供程序的驱动器路径 `<PSDrive>:\Report`，其中 `<PSDrive>` 是提供程序的驱动器 ID。您也可以指定相对路径。例如，点（.）表示当前位置。这样会返回一个用户 ID 和可用的请求类型，您可以使用这些信息与相应的 cmdlet 一起生成更详细的报告。

对于某个特定的用户名（UserName）返回的UserID值，仅适用于通过返回该UserID值时指定的路径（Path）参数所标识的集群。您不能使用该UserID值来识别不同集群中的同一用户。

## 示例

### 示例 1：获取用户的请求报告
```
PS C:\> Get-RmsUserRequestReport -Path "." -UserName "CONTOSO\PFuller"
```

该命令会显示来自Contoso域内用户PFuller的所有请求的汇总报告。

### 示例 2：获取用户的 AcquireLicense 请求报告
```
PS C:\> Get-RmsUserRequestReport -Path "." -StartTime 2/1/2009 -EndTime 2/28/2009 -UserName "CONTOSO\PFuller" -RequestType "AcquireLicense"
```

该命令显示了指定用户为获取许可证而提交的请求信息。

### 示例 3：获取用户请求报告并显示其信息
```
PS C:\> Get-RmsUserRequestReport -Path "." -RequestType "AcquireLicense" -UserName "CONTOSO\PFuller" | Get-RmsRequestInfo -Path "."
```

此命令会显示有关用户申请获取许可证的详细信息。`Get-RmsUserRequestReport` cmdlet 用于检索用户的许可证申请信息，然后将结果传递给 `Get-RmsRequestInfo` cmdlet，以便显示该申请的详细内容。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -EndTime
用于指定系统健康报告的时间段的结束时间。此参数表示一个时间值。有关如何指定时间的详细信息，请参阅*StartTime*参数的描述。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定一个提供者驱动器及其路径，或者当前驱动器上的相对路径。此参数是必需的。使用点（.）来表示当前位置。该参数不支持通配符，也没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequestType
指定用户请求的类型，例如“获取许可证”（Acquire License）、“预认证”（Pre-Certify）以及“获取客户端许可颁发机构证书”（Get Client Licenser Certificate）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -StartTime
指定一个时间段的开始。此参数用于指定一个时间值。

以下示例展示了用于指定时间的常用语法。除非另有说明，否则时间默认为当地时间。当未指定时间值时，时间被视为當地的午夜12点（12:00:00）。当未指定日期时，日期则默认为当前日期。

`2006年4月17日`

2006年4月17日，星期一

下午2点22分45秒

2006年4月17日，星期一，下午2点22分45秒

这些示例指定了相同的日期和时间（但不包括秒数）。

`2006年4月17日 下午2:22`

2006年4月17日，星期一，下午2点22分

下午2点22分

以下示例展示了如何使用RFC1123标准来指定日期和时间。该示例使用格林尼治标准时间（GMT）来定义时间。

`2006年4月17日，星期一，21:22:48 GMT`

以下示例展示了如何将往返时间指定为协调世界时（UTC）。该示例表示的是2006年4月17日星期一下午2点22分48秒（UTC时间）。

`2000-04-17T14:22:48.0000000`

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -UserName
指定您请求用户报告的目标用户，格式为 \<domain_name\>\\\<user_name\>。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsCertChain](./Get-RmsCertChain.md)

[Get-RmsCertInfo](./Get-RmsCertInfo.md)

[Get-RmsRequestInfo](./Get-RmsRequestInfo.md)

