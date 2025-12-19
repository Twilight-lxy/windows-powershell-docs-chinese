---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmMacro.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/get-fsrmmacro?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-FsrmMacro
---

# Get-FsrmMacro

## 摘要
获取由 FSRM 支持的宏。

## 语法

```
Get-FsrmMacro [-Type <FsrmMacroTypeEnum[]>] [-Name <String[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-FsrmMacro` cmdlet 可以获取一个或多个由文件服务器资源管理器（File Server Resource Manager，简称 FSRM）支持的宏，这些宏可用于配置选项。该 cmdlet 会根据你在 `Type` 参数中指定的 FSRM 对象来检索相应的 FSRM 支持的宏。

## 示例

### 示例 1：获取 FSRM 支持的用于配额管理的宏
```
PS C:\> Get-FsrmMacro -Type Quota
```

这个命令可以获取FSRM支持的所有用于配额管理的宏。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的任务。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个宏名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Type
指定一个包含 FSRM 对象类型的数组。该参数的可接受值为：

- Quota
- FileScreen
- FileManagementJob
- ADR

```yaml
Type: FsrmMacroTypeEnum[]
Parameter Sets: (All)
Aliases:
Accepted values: Quota, FileScreen, FileManagementJob, Adr

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### Microsoft.PowerShell.Cmdletization.GeneratedTypes.FsrmMacroTypeEnum[]

### System.String[]

## 输出

### Microsoft.Management.Infrastructure.CimInstance

### Microsoft.Management.Infrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMMacro

## 备注

## 相关链接

[Get-FsrmAdrSetting](./Get-FsrmAdrSetting.md)

[Get-FsrmFileManagementJob](./Get-FsrmFileManagementJob.md)

[Get-FsrmFileScreen](./Get-FsrmFileScreen.md)

[Get-FsrmQuota](./Get-FsrmQuota.md)

