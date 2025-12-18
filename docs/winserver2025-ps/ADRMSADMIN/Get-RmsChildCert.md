---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmschildcert?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsChildCert
---

# Get-RmsChildCert

## 摘要
从用于用户对 AD RMS 集群请求的父证书中返回所有子证书。

## 语法

```
Get-RmsChildCert [-StartTime <DateTime>] [-EndTime <DateTime>] -ParentCertId <String> -ParentCertType <String>
 [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsChildCert` cmdlet 可以从父客户端许可证书（CLC）中获取所有发布的许可证，或者从用于用户请求的父发布许可证中获取所有最终用户许可证（EUL）。这些操作都是在 Active Directory 权限管理服务（AD RMS）集群中进行的。

要获取许可证，请指定您希望从中检索子证书的父证书的 *ParentCertID* 和 *ParentCertType*，然后将 *Path* 参数设置为 AD RMS 提供程序的驱动器路径 `<PSDrive>:\`Report，其中 `<PSDrive>` 是提供程序的驱动器 ID。您也可以指定相对路径。例如，点（.）表示当前位置。

使用 `Get-RmsCertChain` cmdlet 来获取需要检索子证书的证书的 `ParentCertID` 和 `ParentCertType`。返回的 `ParentCertID` 值仅适用于由 `Get-RmsCertChain` 的 `Path` 参数指定的集群。您不能使用同一个 `ParentCertID` 来标识不同集群中的同一证书。

## 示例

### 示例 1：获取某个父证书的所有子证书
```
PS C:\> Get-RmsChildCert -Path "." -ParentCertId "8AGI9GoWuobJDsTmr/CUHTCEpsI=" -ParentCertType CLC
```

该命令会返回父客户端许可证书（parent client licensor certificate）下的所有子证书。

### 示例 2：传递证书 ID 并获取所有子证书
```
PS C:\> $parentCert = Get-RmsCertChain -Path "." -RequestID 3 | Where {$_.CertificateType -eq 'Client-Licensor-Certificate'}
PS C:\> Get-RmsChildCert -Path "." -ParentCertId $parentCert.CertificateID -ParentCertType $parentCert.CertificateType
```

此命令将使用 **Get-RmsCertChain** cmdlet 获取的证书存储在一个变量中，然后利用该变量将证书ID和类型传递给 **Get-RmsChildCert** cmdlet，以获取子证书。

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
用于指定系统健康报告的时间段的结束时间。此参数表示一个时间值。有关如何指定时间的详细信息，请参阅StartTime参数的说明。

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

### -ParentCertId
指定要返回子证书的父证书。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ParentCertType
指定用于返回子证书的父证书类型。该参数的可能取值为“Client-Licensor-Certificate”（简称CLC）或“Issuance-License”（简称IL）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: CLC, Client-Licensor-Certificate, IL, Issuance-License

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定一个提供程序驱动器及其路径，或者是当前驱动器上的相对路径。此参数是必需的。可以使用点（.）来表示当前位置。该参数不支持通配符，也没有默认值。

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

### -StartTime
指定一个时间段的开始点。此参数表示一个时间值。

以下示例展示了用于指定时间的常用语法。除非另有说明，否则时间默认为当地时间。当没有指定时间值时，时间被假定为当天的凌晨12点（即12:00:00 AM）。当没有指定日期时，日期被假定为当前日期。

`2006年4月17日`

2006年4月17日，星期一

下午2点22分45秒

2006年4月17日，星期一，下午2点22分45秒

这些示例指定了相同的日期和时间（但不包括秒数）。

`2006年4月17日 下午2:22`

2006年4月17日，星期一，下午2点22分

下午2点22分

以下示例展示了如何使用RFC1123标准来指定日期和时间。该示例以格林尼治标准时间（GMT）作为时间的参考基准。

`2006年4月17日，星期一，21:22:48 GMT`

以下示例展示了如何将一个往返时间值指定为协调世界时（UTC）。该示例代表的是2006年4月17日星期一下午2点22分48秒（UTC时间）。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsCertChain](./Get-RmsCertChain.md)

[Get-RmsCertInfo](./Get-RmsCertInfo.md)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

