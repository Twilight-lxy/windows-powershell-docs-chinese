---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/export-rmsreportdefinitionlanguage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-RmsReportDefinitionLanguage
---

# Export-RmsReportDefinitionLanguage

## 摘要
导出所有报告定义文件（.rdl格式）。

## 语法

```
Export-RmsReportDefinitionLanguage [-ExportLocation] <String> [-Force] [-Path] <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Export-RmsReportDefinitionLanguage` cmdlet 会为当前版本的 Active Directory Rights Management Services (AD RMS) 导出以下报告定义文件（.rdl 格式）：

- Report_Health_MultiReport.rdl
- Report_TroubleShooting_UserRequestSummary.rdl
- Report_TroubleShooting_UserRequestTypeList.rdl
- Report_TroubleShooting_UserRequestDetail.rdl
- Report_TroubleShooting_UserRequestCertificateInfo.rdl
- Report_TroubleShooting_AllILsFromCLC.rdl.rdl
- Report_TroubleShooting_AllEULsFromIssuanceLicense.rdl

这个cmdlet不会导出Report_TroubleShooting-DecryptILRightsLabel.rdl文件。由于该文件需要一个私钥，因此SQL Server报告服务无法使用它。

要导出报告定义文件，请指定用于保存文件的*ExportLocation*，并将*Path*参数设置为AD RMS提供程序驱动器子目录`<PSDrive>:\Report`，其中`<PSDrive>`是提供程序驱动器的ID。您也可以指定相对路径。例如，点（.）表示当前位置。

## 示例

### 示例 1：导出报告定义文件
```
PS C:\> Export-RmsReportDefinitionLanguage -Path "." -ExportLocation "c:\temp\"
```

这个命令会将报告定义文件导出到 C:\temp\ 目录中。

## 参数

### -Confirm
在运行cmdlet之前会提示您确认是否要执行该操作。

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

### -ExportLocation
指定导出文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Force
如果这些限制不会危及安全性，那么 `Force` 会覆盖那些阻止命令成功的限制。例如，`Force` 可以覆盖只读属性或创建目录以完成文件路径的构建，但它不会尝试更改文件的权限。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定提供程序所在的驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。该参数不支持通配符，且没有默认值。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsSystemHealthReport](./Get-RmsSystemHealthReport.md)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

